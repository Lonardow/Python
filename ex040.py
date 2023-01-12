x = float(input('Digite a primeira nota: '))
y = float(input('Digite a segunda nota: '))
z = float(input('Digite a terceira nota: '))

media = (x+y+z)/3

if media < 5.0:
    print('Reprovado')
elif media >= 5.0 and media <= 6.9:
    print('Recuperação')
elif media > 7.0:
    print('Aprovado')
