somaIdade = 0
oldestMan = 0
oldestManName = ''
womanCount = 0

for c in range(1, 5):

    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [f]/[m]: '))
    somaIdade += idade
    if oldestMan < idade:
        oldestMan = idade
        oldestManName = nome
    if sexo == 'f' and idade < 20:
        womanCount += 1

media = somaIdade/4
print(f'A média de idade do grupo é {media} anos')
print(
    f'O homem mais velho tem {oldestMan} anos e seu nome é {oldestManName}.')
print(f'Ao todo são {womanCount} mulhers com menos de 20 anos.')
