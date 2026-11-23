funcionarios = [
    {"nome": "Ana", "setor": "TI", "salario": 3500},
    {"nome": "Carlos", "setor": "RH", "salario": 2800},
    {"nome": "Mariana", "setor": "TI", "salario": 4200},
    {"nome": "Pedro", "setor": "Financeiro", "salario": 3900}
]

def filtrar_salarios(lista, salarios):
    nomes = []
    for funcionario in lista:
        if funcionario["salario"] >= salarios:
            nomes.append(funcionario["nome"])
    return nomes


print(filtrar_salarios(funcionarios, 5000))