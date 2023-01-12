# lista = []

# for i in range(0, 9):
#     x = int(input('Digite um numero: '))
#     lista.append(x)
# for y in lista:
#     print('[  ', y, '  ]', end='')
#     if y == 3 or y == 6:
#         print('\n', end='')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l,c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
