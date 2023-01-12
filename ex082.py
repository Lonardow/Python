lista = []
pares = []
impares = []

while True:
    x = int(input('Digite um numero: '))
    lista.append(x)
    if x == 0:
        break
for y in lista:
    if y % 2 == 0:
        pares.append(y)
    else:
        impares.append(y)
print(lista)
print('pares', pares)
print('impares', impares)
