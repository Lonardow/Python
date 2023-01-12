x = int(input('digite o 1 comprimento: '))
y = int(input('digite o 2 comprimento: '))
z = int(input('digite o 3 comprimento: '))


if x < y + z and y < x+y and z < y+x:
    print('Pode-se formar um triangulo')
    if x == y == z:
        print('Triangulo equilaterio')
    elif x != y and x != z:
        print('Triangulo escaleno')
    else:
        print('Triangulo isosceles')
else:
    print('Não se pode formar um triangulo')
