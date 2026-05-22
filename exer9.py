import random

alfabeto = []
for i in range(26):
    alfabeto = alfabeto + [chr(ord('a') + i)]

random.shuffle(alfabeto)

letra = input("Qual letra você quer adivinhar a posição? ").lower()
chute = int(input(f"Em qual posição está a letra '{letra}'? (1 a 26): "))

posicao_real = 0
for i in range(26):
    if alfabeto[i] == letra:
        posicao_real = i + 1

if chute == posicao_real:
    print("Acertou!")
else:
    print(f"Errou! A letra '{letra}' está na posição {posicao_real}.")