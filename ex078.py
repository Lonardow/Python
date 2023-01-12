lista = []
maior = menor = 0


for cont in range(0, 5):
    lista.append(int(input('Digite um numero: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        elif lista[cont] < menor:
            menor = lista[cont]

print(lista)
print(f'O menor valor é {menor} nas posiçoes ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}', end=' ')
print()
print(f'O maior valor é {maior}  nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}', end=' ')
