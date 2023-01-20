def aumentar(x, p, form=False):
    result = ((p*x)/100) + x
    return result if form is False else coin(result)


def diminuir(x, p, form=False):
    result = x - ((p*x)/100)
    return result if form is False else coin(result)


def metade(x, form=False):
    result = x/2
    return result if form is False else coin(result)


def dobro(x, form=False):
    result = x*2
    return result if form is False else coin(result)


def coin(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(x, aum, dim):
    print(f'Preço analisado: {coin(x)}')
    print(f'Dobro do preço: {dobro(x,True)}')
    print(f'Metade do preço: {metade(x, True)}')
    print(f'{aum}% de aumento: {aumentar(x, aum,True)}')
    print(f'{dim}% de redução: {diminuir(x, dim,True)}')
