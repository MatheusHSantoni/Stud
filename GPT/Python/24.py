funcionarios = [
    {"nome": "Ana", "setor": "TI", "salario": 3500},
    {"nome": "Carlos", "setor": "RH", "salario": 2800},
    {"nome": "Mariana", "setor": "TI", "salario": 4200},
    {"nome": "Pedro", "setor": "Financeiro", "salario": 3900}
]

def filtrar_funcionario(lista, setor_desejado, salario_minimo):
    nomes = []
    for funcionario in funcionarios:
        if funcionario["setor"] == setor_desejado and funcionario["salario"] >= salario_minimo:
            nomes.append(funcionario["nome"])
    return nomes

print(filtrar_funcionario(funcionarios, "TI", 4000))