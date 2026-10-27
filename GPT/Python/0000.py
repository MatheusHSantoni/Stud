vendas = [150, 80, 220, 45, 300, 120, 60]
total = 0
vendas_100 = 0
lista_100 = []
maior_venda = vendas[0]
quantidade = len(vendas)

for venda in vendas:
  total += venda

  if venda > 100:
    vendas_100 += 1
    lista_100.append(venda)

  if venda > maior_venda:
    maior_venda = venda


calculo = total / quantidade
print(total)
print(vendas_100)
print(lista_100)
print(maior_venda)
print(calculo)