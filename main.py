número = int(input("Digite um número: "))
for i in range(1, número+1):
    if i**2 <= número:
        print(i**2)
    else:
        break