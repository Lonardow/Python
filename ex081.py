lista = []

while True:
    x = int(input('Digite um numero ou [0] para terminar: '))
    if x == 0:
        break
    else:
        lista.append(x)

lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

if 5 in lista:
    print('O valor 5 esta na lista na posição')
