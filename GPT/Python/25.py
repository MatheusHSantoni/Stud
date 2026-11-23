funcionarios = [
    {"nome": "Ana", "setor": "TI", "salario": 3500},
    {"nome": "Carlos", "setor": "RH", "salario": 2800},
    {"nome": "Mariana", "setor": "TI", "salario": 4200},
    {"nome": "Pedro", "setor": "Financeiro", "salario": 3900}
]

def maior_salario(nome_informado, salario_informado):
  nome = []
  salario = 0

  for funcionario in lista:
    if funcionario["nome"] == nome_informado and funcionario["salario"] == salario_informado:
      nome.append(funcionario["nome"])
      salario += funcionario["salario"]
  return nome, salario