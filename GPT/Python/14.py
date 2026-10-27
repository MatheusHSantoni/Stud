precos = [50, 120, 200, 80, 300]
"""
Preços abaixo de R$ 100: sem desconto.
Preços de R$ 100 até R$ 200, inclusive: desconto de 10%. preco * 0.90
Preços acima de R$ 200: desconto de 20%. preco * 0.80
"""

def aplicar_desconto(lista):
    preco_com_desconto = []
    D10 = 0.90
    D20 = 0.80

    for valor in lista:
        if valor < 100:
            preco_com_desconto.append(valor)

        elif 100 <= valor <= 200:
            preco_com_desconto.append(valor * D10)

        else:
            preco_com_desconto.append(valor * D20)

    return preco_com_desconto
preco_com_desconto = aplicar_desconto(precos) 

print(preco_com_desconto)