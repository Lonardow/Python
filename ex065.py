

x = ''
soma = count = maior = 0
while x != 'n':
    val = int(input('Digite um numero inteiro: '))
    soma += val
    count += 1
    if count == 1:
        maior = menor = val
    else:
        if val > maior:
            maior = val
        if val < menor:
            menor = val
    x = input('Quer continuar? [S/N]')
media = soma/count
print(
    f'Você digitou {count} valores\nA média dos valores é {media}\nO maior {maior} e o menor {menor}')
