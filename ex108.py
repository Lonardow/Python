import moeda
x = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.coin(x)} é {moeda.coin(moeda.metade(x))}')
print(f'O dobro de {moeda.coin(x)} é {moeda.coin(moeda.dobro(x))}')
print(f'Aumentando 10%, temos {moeda.coin(moeda.aumentar(x, 10))}')
print(f'Diminuindo 13%, temos {moeda.coin(moeda.diminuir(x, 13))}')
