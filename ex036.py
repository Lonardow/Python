valor = int((input('DIGITE O VALOR DA CASA: ')))
salario = int((input('DIGITE SEU SALÁRIO: ')))
tempo = int(input('EM QUANTOS ANOS VAI PAGAR: '))
1
prestMax = salario*(30/100)
parcelas = tempo*12

if valor/parcelas <= prestMax:
    print('voce consegue o emprestimo')
else:
    print('não consegue')
