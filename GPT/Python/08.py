vendas = [150, 80, 220, 45, 300, 120, 60]

def analisar_vendas(lista):
  total = 0
  vendas_acima_100 = 0

  for venda in lista:
    total += venda

    if venda > 100:
      vendas_acima_100 += 1

  return total, vendas_acima_100


print(analisar_vendas(vendas))