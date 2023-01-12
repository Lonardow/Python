# x = [int(x) for x in input('Digite um inteiro: ').split()]
# x = 0
x = 0
soma = x
count = 0
while x != 999:
    x = int(input('Digite um inteiro: '))
    if x == 999:
        break
    soma += x
    count += 1
print(f'A soma dos {count} valores inseridos é {soma}')
