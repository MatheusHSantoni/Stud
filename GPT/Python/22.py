funcionarios = [
    {"nome": "Ana", "setor": "TI", "salario": 3500},
    {"nome": "Carlos", "setor": "RH", "salario": 2800},
    {"nome": "Mariana", "setor": "TI", "salario": 4200},
    {"nome": "Pedro", "setor": "Financeiro", "salario": 3900}
]

def filtrar_funcionarios(lista, setor_desejado):
    nomes = []
    for funcionario in lista:
        if funcionario["setor"] == setor_desejado:
            nomes.append(funcionario["nome"])
    return nomes

print(filtrar_funcionarios(funcionarios, "TI"))