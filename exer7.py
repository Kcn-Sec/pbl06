vetor = [0] * 100
for i in range(100):
    vetor[i] = i + 1

print("Números pares de 1 a 100:")
for i in range(100):
    if vetor[i] % 2 == 0:
        print(vetor[i], end=" ")