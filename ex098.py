import time

v = 0


def contador(i, f, p):
    if p == 0:
        p = 1
    if f > i:
        cont = i
        while f >= cont:
            time.sleep(0.5)
            print(cont, end=' ')
            cont += abs(p)
        print('FIM')

    else:
        cont = i
        while cont >= f:
            time.sleep(0.5)
            print(cont, end=' ')
            cont -= abs(p)
        print('FIM')


ini = int(input('Inicio: '))
fin = int(input('Fim: '))
pas = int(input('Passo: '))

contador(ini, fin, pas)
