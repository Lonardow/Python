import moeda

x = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.coin(x)} é {moeda.metade(x, False)}')
print(f'O dobro de {moeda.coin(x)} é {moeda.dobro(x,True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(x, 10,True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(x, 13,False)}')
