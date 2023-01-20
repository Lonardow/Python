import moeda

x = float(input('Digite o preço: R$'))
print(f'A metade de {x} é {moeda.metade(x)}')
print(f'O dobro de {x} é {moeda.dobro(x)}')
print(f'Aumentando 10%, temos {moeda.aumentar(x, 10)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(x, 13)}')
