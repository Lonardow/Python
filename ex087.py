matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = par = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(
            input(f'Digite um valor para a posição [{l,c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if matriz[1][c] > maior:
            maior = matriz[l][c]
        if matriz[l][2] > 0:
            soma += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos valores pares é {par}')
print(f'a soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')
