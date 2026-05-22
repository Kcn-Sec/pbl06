pares   = [0] * 5
impares = [0] * 5

for i in range(5):
    pares[i]   = (i + 1) * 2
    impares[i] = (i * 2) + 1

união = pares + impares

print(f"Pares:   {pares}")
print(f"Ímpares: {impares}")
print(f"Pares e Ímpares:   {união}")