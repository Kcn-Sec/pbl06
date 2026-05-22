palavras = ["banana", "uva", "morango", "abacaxi", "kiwi", "maracujá"]

mais_longa = palavras[0]
mais_curta = palavras[0]

for i in range(len(palavras)):
    if len(palavras[i]) > len(mais_longa):
        mais_longa = palavras[i]
    if len(palavras[i]) < len(mais_curta):
        mais_curta = palavras[i]

print(f"Lista: {palavras}")
print(f"Palavra mais longa: {mais_longa}")
print(f"Palavra mais curta: {mais_curta}")