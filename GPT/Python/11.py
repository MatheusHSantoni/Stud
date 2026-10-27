estoque = [12, 3, 0, 8, 2, 15, 0, 6]

def analisar_estoque(lista):
  quantidade_0 = 0
  baixo_estoque = 0
  soma = 0

  for q in lista:
    soma += q
    
    if q == 0:
      quantidade_0 += 1

# Uma melhoria  => elif 0 < q < 5:
    elif q > 0 and q < 5:
      baixo_estoque += 1

  return soma, quantidade_0, baixo_estoque
soma, quantidade_0, baixo_estoque = analisar_estoque(estoque)

print(soma)
print(quantidade_0)
print(baixo_estoque)