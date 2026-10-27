notas = [8, 5, 9, 4, 7, 10, 6]


def analisar_notas(lista):
  aprovados = 0
  reprovados = 0
  quantidade = len(lista)
  soma = 0
  
  for nota in lista:
    soma += nota

    if nota >= 7:
      aprovados += 1
      
    else:
      reprovados += 1
        
  calculo = soma / quantidade
  return aprovados, reprovados, calculo

aprovados, reprovados, calculo = analisar_notas(notas)

print(f"Média: {calculo}")
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")
