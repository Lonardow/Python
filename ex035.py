# cumprimentos = input(
#     'Digite o comprimento de 3 retas para verificar se podem formar um triangulo: ').split()


# print(max(cumprimentos))

x = int(input('digite o 1 comprimento: '))
y = int(input('digite o 2 comprimento: '))
z = int(input('digite o 3 comprimento: '))

if x < y + z and y < x+y and z < y+x:
    print('Pode-se formar um triangulo')
else:
    print('Não se pode formar um triangulo')
