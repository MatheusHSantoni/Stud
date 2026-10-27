def verificar_idade(idade):
  if idade >= 18:
    return 'Maior de idade!'
  else:
    return 'Menor de idade!  '

print(verificar_idade(20))
print(verificar_idade(15))
print(verificar_idade(18))

""" Sugestão de como poderia ficar, (Removendo o IF)
def verificar_idade(idade):
  if idade >= 18:
    return 'Maior de idade!'

    
  return 'Menor de idade!'
"""