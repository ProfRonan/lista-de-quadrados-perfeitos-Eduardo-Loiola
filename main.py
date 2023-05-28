num_quadrados_perfeitos = int(input("Digite um número: "))
i = 1
contagem = 0
while contagem < num_quadrados_perfeitos:
    if (int(i ** 0.5)) ** 2 == i:
        print(i)
        contagem += 1
    i += 1
