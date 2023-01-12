pessoas = []
grupo = []
maior = menor = 0
x = ''
while True:
    pessoa = str(input('Digite seu nome: '))
    if pessoa == 'z':
        break
    peso = int(input('Digite seu peso: '))
    if len(grupo) == 0:
        maior = menor = peso

    pessoas.append(pessoa)
    pessoas.append(peso)

    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
    for p in pessoas:
        grupo.append(pessoas[:])
        pessoas.clear()
print(pessoas)
print(f'Foram cadastradas {len(grupo)} pessoas')
print(f'O maior peso foi de {maior}KG. Peso de ', end='')
for x in grupo:
    if x[1] == maior:
        print(f'{x[0]}', end=' ')
print()
print(f'O maior peso foi de {menor}KG. Peso de ', end='')
for x in grupo:
    if x[1] == menor:
        print(f'{x[0]}', end=' ')
