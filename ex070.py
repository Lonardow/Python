soma = maisdmil = maisbarato = count = 0
cheapname = ''
while True:
    nome = str(input('Digite o nome de um produto: '))
    preco = float(input('Digite o valor desse produto: '))
    continuar = str(input('Você deseja continuar? [S/N]: ')).lower()[0]
    count += 1
    soma += preco
    if count == 1 or preco < maisbarato:
        maisbarato = preco
        cheapname = nome
    if preco > 1000:
        maisdmil += 1

    if continuar == 'n':
        break
print(
    f'total {soma}, {maisdmil} produtos custam mais de mil reais, {cheapname} é o produto mais barato')
