from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

funcionarios = [
    {"id": 1, "nome": "Ana", "setor": "RH"},
    {"id": 2, "nome": "Carlos", "setor": "TI"},
    {"id": 3, "nome": "Marina", "setor": "Financeiro"}
]


def buscar_funcionario(id_funcionario):
    for funcionario in funcionarios:
        if funcionario["id"] == id_funcionario:
            return funcionario

    return None


@app.get("/")
def inicio():
    return {"mensagem": "Minha primeira API"}


@app.get("/funcionarios/{id_funcionario}")
def consultar_funcionario(id_funcionario: int):
    resultado = buscar_funcionario(id_funcionario)

    if resultado is None:
        raise HTTPException(
            status_code=404, detail="Funcionário não encontrado")

    return resultado

@app.get("/funcionarios")
def listar_funcionarios():
    return funcionarios


class FuncionarioCreate(BaseModel):
    nome: str
    setor: str

@app.post("/funcionarios", status_code=201)
def criar_funcionario(dados: FuncionarioCreate):
    novo_id = max(
        (funcionario["id"] for funcionario in funcionarios),
        default=0) + 1

    novo_funcionario = {
        "id": novo_id,
        "nome": dados.nome,
        "setor": dados.setor
    }

    funcionarios.append(novo_funcionario)
    return novo_funcionario

@app.put("/funcionarios/{id_funcionario}")
def atualizar_funcionario(id_funcionario: int, dados: FuncionarioCreate):
    funcionario = buscar_funcionario(id_funcionario)
    if funcionario is None:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    funcionario["nome"] = dados.nome
    funcionario["setor"] = dados.setor
    return funcionario

@app.delete("/funcionarios/{id_funcionario}")
def excluir_funcionario(id_funcionario: int):
    funcionario = buscar_funcionario(id_funcionario)

    if funcionario is None:
        raise HTTPException(
            status_code=404,
            detail="Funcionário não encontrado"
        )

    funcionarios.remove(funcionario)

    return {"mensagem": "Funcionário excluído com sucesso"}
