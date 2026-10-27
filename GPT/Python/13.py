pedidos = [120, 50, 300, 80, 200, 40, 150]

def analisar_pedidos(lista):
  v_total = 0
  acima_100 = 0
  menores_100 = []
   
  for pedido in lista:
    v_total += pedido 

    if pedido >= 100:
      acima_100 += 1
    else:
      menores_100.append(pedido)
  return v_total, acima_100, menores_100
v_total, acima_100, menores_100 = analisar_pedidos(pedidos)

print(v_total)
print(acima_100)
print(menores_100)
        