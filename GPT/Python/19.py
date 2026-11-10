produto = {
    "nome": "Notebook",
    "preco": 3500,
    "estoque": 8
}
def analisar_produto(produto):
    nome = produto["nome"]
    preco = produto["preco"]
    estoque = produto["estoque"]
    total = preco * estoque

    if estoque < 10:
        mensagem = 'Estoque baixo'
    else:
        mensagem = 'Estoque suficiente'

    return nome, total, estoque, mensagem

nome, total, estoque, mensagem = analisar_produto(produto)
print(f'Produto: {nome}, Total em estoque: R${total}, Estoque: {estoque}, Status: {mensagem}')