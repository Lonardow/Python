
x = int(input('Digite o 1 numero'))
y = int(input('Digite o 2 numero'))
z = int(input('Digite o 3 numero'))

maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = z
print(f'O maior valor foi {maior}')

menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z
print(f'O menor é {menor}')
