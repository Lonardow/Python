ano = int(input('Digite um ano para saber se ele é bissexto: '))

if ano % 4 == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')
