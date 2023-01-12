inp = int(input('Digite um numero para saber se ele é primo ou não: '))

for c in range(2, inp):
    if inp % c == 0:
        print(f'{inp} não é um numero primo')
        break
    else:
        print(f'{inp} é um numero primo')
        break
