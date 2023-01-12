import random

inp = input('Digite Pedra papel ou tesoura: ')

poss = ['pedra', 'papel', 'tesoura']
cpu = poss[random.randint(0, 2)]

print(inp, cpu)


if cpu == 'pedra' and inp == 'tesoura' or cpu == 'papel' and inp == 'pedra' or cpu == 'tesoura' and inp == 'papel':
    print('Você perdeu')
elif cpu == inp:
    print('Empate')
else:
    print('Voce Ganhou')
