inp = int(input('Digite um numero: '))
base = input('Qual a base voce quer? Binario, octal ou hexadecimal: ')

if base == 'binario':
    inp = format(inp, 'b')
    print(inp)
elif base == 'octal':
    inp = format(inp, 'o')
    print(inp)
elif base == 'hexadecimal':
    inp = format(inp, 'x')
    print(inp)
else:
    ('voce não escolheu uma opção correta')
