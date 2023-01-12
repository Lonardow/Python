extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    inp = int(input('Digite um numero para ver sua escrita por extenso: '))
    while inp not in range(0, 21):
        inp = int(
            input('Tente novamente. Digite um numero para ver sua escrita por extenso: '))
    print(f'Você digitou o numero {extenso[inp]}')
