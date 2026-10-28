palavras = ["Python", "Java", "HTML", "JavaScript", "SQL", "Docker"]

def analisar_palavra(lista):
  long_word = []
  short_word = []
  total = 0

  for word in lista:
    total += len(word)
    if len(word) >=  6:  
      long_word.append(word)
    else:
      short_word.append(word)
  return total, long_word, short_word

total, long_word, short_word = analisar_palavra(palavras)

print(total)
print(long_word)
print(short_word)
