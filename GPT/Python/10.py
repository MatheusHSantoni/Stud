temperaturas = [28, 35, 22, 31, 19, 40, 26]

def analisar_temperaturas(lista):
  maior_temperatura = lista[0]
  menor_temperatura = lista[0]
  acima_30 = 0

  for t in lista:
    if t > maior_temperatura:
        maior_temperatura = t

    if t < menor_temperatura:
        menor_temperatura = t

    if t > 30:
        acima_30 += 1

  return maior_temperatura, menor_temperatura, acima_30
maior_temperatura, menor_temperatura, acima_30 = analisar_temperaturas(temperaturas)

print(f"Maior Temperatura: {maior_temperatura}")
print(f"Menor Temperatura: {menor_temperatura}")
print(f"Temperaturaturas acima de 30º : {acima_30}")