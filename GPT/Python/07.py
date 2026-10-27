numeros = [3, 8, 12, 5, 16, 7, 20]

def filtrar_pares(lista):
  lista_pares = []
  for numero in lista:

    if numero % 2 == 0:
      lista_pares.append(numero)

  return lista_pares

print(filtrar_pares(numeros))
