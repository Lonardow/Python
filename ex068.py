import random
count = 0

while True:
    player = int(input('Digite um numero: '))
    escolha = input(
        'Escolha entre [P] para par ou [I] para impar: ').lower()[0]
    cpu = random.randint(0, 10)
    soma = cpu + player

    print(
        f'Você jogou {player} e o computador {cpu}. Total de {soma}!!!')
    if escolha == 'p':
        if soma % 2 == 0:
            print('Você GANHOU!')
            count += 1
        else:
            print('Você PERDEU')
            break
    elif escolha == 'i':
        if soma % 2 == 1:
            print('Você GANHOU!')
            count += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente')
print(f'Game over!!! Voce acertou {count} vezes')
