import random
import time

lista = []


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    while len(lista) < 5:
        lista.append(random.randint(0, 20))
    for x in lista:
        print(x, end=' ')
        time.sleep(0.5)
    print('PRONTO!', end='')


sorteia()

print()


def somaPar():
    soma = 0
    time.sleep(0.5)
    print(f'Somando os valores pares de {lista}, ', end=' ')
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'temos {soma}')


somaPar()
