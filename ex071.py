cinc = vint = dez = um = 0

while True:
    valor = int(input('Qual o valor que deseja sacar? '))
    total = valor
    if valor > 50:
        cinc = valor // 50
        valor = valor - (cinc*50)
        print(f'Serão impressas pelo caixa eletronico {cinc} notas de R$50')
    if valor > 20:
        vint = valor // 20
        valor = valor - (vint*20)
        print(f'Serão impressas pelo caixa eletronico {vint} notas de R$20')
    if valor > 10:
        dez = valor // 10
        valor = valor - (dez*10)
        print(f'Serão impressas pelo caixa eletronico {dez} notas de R$10')
    if valor > 1:
        um = valor // 1
        print(f'Serão impressas pelo caixa eletronico {um} notas de R$1')
    print(f'Totalizando R${total}')
