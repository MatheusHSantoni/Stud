#!/usr/bin/env python3
"""Baixa e consolida partidas públicas do Chess.com em formato PGN."""

import argparse
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API = "https://api.chess.com/pub/player"
MAX_TENTATIVAS = 5
INTERVALO_REQUISICOES = 0.25
ERROS_TEMPORARIOS = {429, 500, 502, 503, 504}
PADRAO_ARQUIVO = re.compile(r"/games/(\d{4})/(0[1-9]|1[0-2])/?$")


def baixar(url: str, usuario: str) -> bytes:
    """Faz uma requisição HTTP, repetindo em caso de falha temporária."""
    headers = {
        "User-Agent": f"ChessHistoryDownloader/1.0 (user: {usuario}; personal archival)",
        "Accept": "application/json, application/x-chess-pgn, text/plain",
    }

    for tentativa in range(1, MAX_TENTATIVAS + 1):
        try:
            with urlopen(Request(url, headers=headers), timeout=40) as resposta:
                return resposta.read()
        except HTTPError as erro:
            if erro.code not in ERROS_TEMPORARIOS or tentativa == MAX_TENTATIVAS:
                raise RuntimeError(f"Erro HTTP {erro.code} em {url}") from erro
        except (URLError, TimeoutError) as erro:
            if tentativa == MAX_TENTATIVAS:
                raise RuntimeError(f"Falha de conexão em {url}: {erro}") from erro

        espera = min(2 ** (tentativa - 1), 20)
        print(f"  Tentativa {tentativa} falhou. Repetindo em {espera}s...")
        time.sleep(espera)

    raise RuntimeError("Falha inesperada na requisição")


def obter_periodos(usuario: str) -> list[str]:
    """Retorna os meses disponíveis em ordem cronológica."""
    url = f"{API}/{usuario}/games/archives"
    dados = json.loads(baixar(url, usuario))

    if not isinstance(dados, dict) or not isinstance(dados.get("archives"), list):
        raise ValueError("Resposta inesperada da API: lista de arquivos ausente")

    periodos = []
    for url_arquivo in dados["archives"]:
        if not isinstance(url_arquivo, str):
            raise ValueError("A API retornou um endereço de arquivo inválido")
        resultado = PADRAO_ARQUIVO.search(url_arquivo)
        if resultado is None:
            raise ValueError(f"Endereço de arquivo inesperado: {url_arquivo}")
        ano, mes = resultado.groups()
        periodos.append(f"{ano}-{mes}")

    return sorted(set(periodos))


def salvar_atomicamente(caminho: Path, conteudo: str) -> None:
    """Substitui o arquivo apenas depois de escrever o conteúdo completo."""
    temporario = caminho.with_suffix(caminho.suffix + ".tmp")
    try:
        temporario.write_text(conteudo, encoding="utf-8")
        temporario.replace(caminho)
    finally:
        temporario.unlink(missing_ok=True)


def baixar_mes(usuario: str, periodo: str, pasta: Path) -> None:
    """Baixa, valida e salva o PGN de um mês."""
    ano, mes = periodo.split("-")
    url = f"{API}/{usuario}/games/{ano}/{mes}/pgn"
    conteudo = baixar(url, usuario).decode("utf-8-sig").strip()

    if not re.search(r'^\[Event\s+"', conteudo, re.MULTILINE):
        raise ValueError(f"O arquivo PGN de {periodo} veio vazio ou inválido")

    salvar_atomicamente(pasta / f"{periodo}.pgn", conteudo + "\n")


def consolidar(periodos: list[str], pasta: Path, saida: Path) -> int:
    """Une arquivos mensais sem carregar todo o histórico na memória."""
    temporario = saida.with_suffix(saida.suffix + ".tmp")
    total = 0

    try:
        with temporario.open("w", encoding="utf-8", newline="\n") as destino:
            for periodo in periodos:
                with (pasta / f"{periodo}.pgn").open("r", encoding="utf-8-sig") as origem:
                    for linha in origem:
                        destino.write(linha)
                        if linha.startswith('[Event "'):
                            total += 1
                destino.write("\n")
        temporario.replace(saida)
    finally:
        temporario.unlink(missing_ok=True)

    return total


def principal() -> None:
    parser = argparse.ArgumentParser(description="Baixa partidas PGN públicas do Chess.com")
    parser.add_argument("--usuario", default="pxmath", help="Nome de usuário no Chess.com")
    parser.add_argument("--atualizar-tudo", action="store_true", help="Baixa novamente todos os meses")
    args = parser.parse_args()

    usuario = args.usuario.strip()
    if not re.fullmatch(r"[A-Za-z0-9_-]+", usuario):
        parser.error("O nome de usuário contém caracteres inválidos")

    print(f"Buscando histórico de {usuario}...")
    periodos = obter_periodos(usuario)
    if not periodos:
        print("Nenhum mês com partidas finalizadas foi encontrado.")
        return

    pasta = Path(f"partidas_{usuario}")
    pasta.mkdir(parents=True, exist_ok=True)
    saida = Path(f"{usuario}_todas_partidas.pgn")
    mes_atual = datetime.now(timezone.utc).strftime("%Y-%m")
    ultimo_mes = periodos[-1]
    baixados = 0

    for indice, periodo in enumerate(periodos, start=1):
        arquivo = pasta / f"{periodo}.pgn"
        atualizar = (
            args.atualizar_tudo
            or not arquivo.is_file()
            or periodo == mes_atual
            or periodo == ultimo_mes
        )

        if atualizar:
            print(f"[{indice}/{len(periodos)}] Baixando {periodo}...")
            baixar_mes(usuario, periodo, pasta)
            baixados += 1
            time.sleep(INTERVALO_REQUISICOES)
        else:
            print(f"[{indice}/{len(periodos)}] {periodo} já salvo")

    total = consolidar(periodos, pasta, saida)
    print(f"\nConcluído! {total} partidas em {len(periodos)} meses.")
    print(f"PGN consolidado: {saida.resolve()}")
    print(f"Arquivos mensais: {pasta.resolve()}")
    print(f"Meses baixados ou atualizados: {baixados}")


if __name__ == "__main__":
    try:
        principal()
    except (RuntimeError, ValueError, OSError) as erro:
        raise SystemExit(f"Erro: {erro}") from erro
