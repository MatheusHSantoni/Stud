salarios = [1800, 2500, 3200, 1500, 4100, 2800, 1200]

def analisar_salarios(lista):
  maior_salario = lista[0]
  menor_salario = lista[0]
  quantidade = len(lista)
  acima_2500 = 0
  soma = 0

  for salario in lista:
    soma += salario
    calculo = soma / quantidade

    if salario > maior_salario:
      maior_salario = salario

    if salario < menor_salario:
      menor_salario = salario

    if salario > 2500:
      acima_2500 += 1

    
  return maior_salario, menor_salario, acima_2500, calculo
maior_salario, menor_salario, acima_2500, calculo = analisar_salarios(salarios)

print(maior_salario)
print(menor_salario)
print(acima_2500)
#print(f'{calculo:.2f}')