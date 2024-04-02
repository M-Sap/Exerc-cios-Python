h = 0
m = 0
MaisVelho=0
MaisNovo= float('inf')

n = int(input("Digite o número de pessoas: "))

for x in range(1, n+1):
    nome = input("Digite o nome: ")
    sexo = input("H - Homem ou M - Mulher: ").upper()
    idade = int(input("Digite a idade: "))



    if sexo == "H":
        print(nome, "é Homem!")
        h += 1
        if idade> MaisVelho:
            MaisVelho= idade
    elif sexo == "M":
        print(nome, "é Mulher!")
        m += 1
        if idade< MaisNovo:
            MaisNovo= idade
    else:
        print("Sexo só pode ser H ou M!")

print("Foram inseridos", h, "Homens")
print("Foram inseridos", m, "Mulheres")
print("A idade da pessoa mais velha é: ", MaisVelho)
print("A idade da pessoa mais nova é: ", MaisNovo)
