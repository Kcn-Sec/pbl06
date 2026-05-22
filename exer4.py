vetor = [0] * 10
for i in range(10):
    vetor[i] = i + 1

print("Lista em ordem reversa:")
for i in range(9, -1, -1):
    print(vetor[i], end=" ")