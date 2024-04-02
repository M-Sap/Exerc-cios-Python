N = int(input("Digite o tamanho da sua array: "))
vetor1 = []
invertido= [0] * N  # Cria uma lista com N elementos, todos inicializados como 0

# Preenchendo vetOriginal com valores inseridos pelo usuário
for i in range(N):
    num = int(input("Digite um número: "))
    vetor1.append(num)

# Invertendo a lista vetOriginal e armazenando em vetInvert
for i in range(N):
    invertido[i] = vetor1[N - i - 1]

# Exibindo o vetor invertido
print("O vetor invertido é:")
for num in invertido:
    print(num)
