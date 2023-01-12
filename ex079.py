x = 0
lista = []

while True:
    x = int(input('Digite um valor: '))
    if x in lista:
        print('Esse ja foi digitado, digite outro: ')
    else:
        lista.append(x)
        print('Item adicionado com sucesso')
    y = str(input('Quer continuar? [S/N]'))
    if y in 'Nn':
        break
lista.sort()
print(f'Você digitou os valores {lista}')
