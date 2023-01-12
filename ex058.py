import random
print('pensei em um numero, de 0 a 10 tente adivinhar')

randNumber = random.randint(0, 10)

number = 0

while number != randNumber:
    number = int(input('Digite um numero: '))
else:
    print(f'Você acertou !!! O numero era {randNumber}')
