preco = float(input('Digite o valor do produto: '))
pag = input('Digite a forma de pagamento 1-dinheiro, 2-debito, 3-em duas vezes no credito, 4- em tres vezes ou mais no credito: ')

if pag == '1':
    print(f'o valor será R${preco - (preco*(10/100))}')
elif pag == '2':
    print(f'o valor será R${preco - (preco*(5/100))}')
elif pag == '3':
    print(f'o valor sera R${preco}')
elif pag == '4':
    print(f'o valor sera R${preco + (preco*(20/100))}')
