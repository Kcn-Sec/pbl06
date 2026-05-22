vetor = [0] * 10
for i in range(10):
    vetor[i] = (i + 1) ** 2

soma = 0
for i in range(10):
    soma += vetor[i]

print(f"Lista: {vetor}")
print(f"Soma total: {soma}")