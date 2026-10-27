alunos = ["Ana", "Carlos", "Mariana", "João", "Pedro"]

def filtrar_nomes(lista):
    mais_5_caracteres = []
    menos_5_caracteres = []

    for nome in lista:
        if len(nome) > 5:
            mais_5_caracteres.append(nome)
        else:
            menos_5_caracteres.append(nome)

    return mais_5_caracteres, menos_5_caracteres

mais_5_caracteres, menos_5_caracteres = filtrar_nomes(alunos)

print(mais_5_caracteres)
print(menos_5_caracteres)