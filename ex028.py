import random
print('pensei em um numero, de 0 a 10 tente adivinhar')

randNumber = random.randint(0, 10)

number = int(input('Digite um numero: '))

if number == randNumber:
    print('Você acertou !!!')
else:
    print(f'Você errou o numero foi {randNumber}')
