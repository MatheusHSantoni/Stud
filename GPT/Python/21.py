funcionarios = [
    {"nome": "Ana", "setor": "TI", "salario": 3500},
    {"nome": "Carlos", "setor": "RH", "salario": 2800},
    {"nome": "Mariana", "setor": "TI", "salario": 4200},
    {"nome": "Pedro", "setor": "Financeiro", "salario": 3900},
    {"nome": "Julia", "setor": "TI", "salario": 3100}
]

def analisar_funcionarios(funcionarios):
  total_salario = 0
  qtd_funcionarios = 0
  nome_funcionarios = []
  maior_salario = funcionarios[0]["salario"]

  
  for funcionario in funcionarios:
    nome = funcionario["nome"]
    setor = funcionario["setor"]
    salario = funcionario["salario"]
    total_salario += salario

    if setor == "TI":
      nome_funcionarios.append(nome)
      qtd_funcionarios += 1

    if salario > maior_salario:
      maior_salario = salario
  return total_salario, qtd_funcionarios, nome_funcionarios, maior_salario
total_salario, qtd_funcionarios, nome_funcionarios, maior_salario = analisar_funcionarios(funcionarios)

print(total_salario)
print(qtd_funcionarios)
print(nome_funcionarios)
print(maior_salario)