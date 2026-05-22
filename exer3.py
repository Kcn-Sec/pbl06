frase = input("Digite uma frase: ")

palavras = frase.split()

lista = [' '] * len(palavras)

for i in range(len(palavras)):
    lista[i] = palavras[i]

print(lista)