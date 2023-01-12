grupo = [[], []]

for i in range(0, 7):
    x = int(input('Digite um valor: '))

    if x % 2 == 0:
        grupo[0].append(x)
    else:
        grupo[1].append(x)
grupo[0].sort()
grupo[1].sort()

print(grupo)
