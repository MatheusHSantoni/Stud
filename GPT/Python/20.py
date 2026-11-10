produtos = [
    {"nome": "Notebook", "preco": 3500, "estoque": 8},
    {"nome": "Mouse", "preco": 80, "estoque": 25},
    {"nome": "Teclado", "preco": 150, "estoque": 4},
    {"nome": "Monitor", "preco": 1200, "estoque": 12}
]
def analisar_estoque(produtos):
    estoque_baixo = []
    total = 0
    for produto in produtos:
        nome = produto["nome"]
        preco = produto['preco']
        estoque = produto['estoque']
        total += preco * estoque

        if estoque < 10:
            estoque_baixo.append(nome)

    return total, len(estoque_baixo), estoque_baixo
total, quantidade, estoque_baixo = analisar_estoque(produtos)

print(total)
print(quantidade)
print(estoque_baixo)