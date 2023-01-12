# list = (int(x) for x in input('Digite quatro numeros: ').split())

# print(list)

# inp = input('Digite uma lista de numeros separados por espaço: ')

# list = tuple(int(item) for item in inp.split())

# print(list)

list = (int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')))

print(f'Você digitou os valores {list}')

if 9 in list:
    print(f'O numero 9 apareceu {list.count(9)} veze(s)')
if 3 in list:
    print(f'O valor 3 apareceu na {list.index(3)+1}ª posição')
print(f'Os valores pares digitados foram ', end='')
for item in list:
    if item % 2 == 0:
        print(item, end=' ')
