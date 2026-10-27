numeros = [10, 7, 4, 9, 12, 3, 8]

def analisar_numeros(lista):
    numeros_pares = 0

    for numero in lista:
        if numero % 2 == 0:
            numeros_pares += 1

    return numeros_pares

print(analisar_numeros(numeros))