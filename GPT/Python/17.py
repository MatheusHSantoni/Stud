numeros = []
numeros1 = [10, 20, 30]

def calcular_media(lista):
    if len(lista) == 0:
        return "Lista vazia"

    soma = 0

    for n in lista:
        soma += n

    calculo = soma / len(lista)
    return calculo

print(calcular_media(numeros))
print(calcular_media(numeros1))