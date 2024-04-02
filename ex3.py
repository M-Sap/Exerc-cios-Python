n = int(input("Digite o número para ser verificado: "))
resultado = 0

if n <= 1:
    print("Esse número não primo")

for i in range(2, n// 2 + 1):
    if n % i == 0:
        resultado += 1
        break

if resultado == 0:
    print(n, "é um número primo")
else:
    print(n, "não é um número primo")