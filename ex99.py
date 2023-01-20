import time


def maior(* num):
    maior = 0
    lista = list(num)
    for val in lista:
        if val > maior:
            maior = val
        print(val, end=' ')
        time.sleep(0.5)
    print(f'Foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 3, 5, 7, 1)
