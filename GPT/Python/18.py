notas = [8, 5, 10, 4, 7, 6, 9]

def analisar_notas(lista):
    if len(lista) == 0:
        return "Lista vazia"

    soma = 0
    maior_sete = 0
    menor_sete = 0
    maior_nota = lista[0]

    for n in lista:
        soma += n

        if n >= 7:
            maior_sete += 1
        else:
            menor_sete += 1

        if n > maior_nota:
            maior_nota = n

    calculo = soma / len(lista)
    return calculo, maior_sete, menor_sete, maior_nota


print(analisar_notas(notas))
print(analisar_notas([]))