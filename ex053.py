frase = input('Digite uma frase para verificar se é um palindromo: ')

# for count in range(0, 3):
#     x = frase[count]
#     x[::-1]
#     y = []
#     print(' '.join(x.frase))

pal = frase[::-1]

if frase == pal:
    print(f'{frase} é um palindromo')
else:
    print(f'{frase} não é um palindromo')
