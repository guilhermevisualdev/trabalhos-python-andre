# números da sequência de Fibonacci
fibonacci = [0, 1]  # Inicia a sequência com os dois primeiros números (0 e 1)

for i in range(2, 20): # gera/limita até os 20 primeiros
    proximo = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(proximo)

# cálculo da soma dos números da sequência
soma = sum(fibonacci)

# resultados
print("Os 20 primeiros números da sequência de Fibonacci:")
print(fibonacci)
print(f"\nSoma dos números: {soma}")