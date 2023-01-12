
brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo',
               'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará',
               'Atlético-GO', 'Avaí', 'Juventude')

goias = brasileirao.index('Goiás')

print(f'Os cinco primeiros colocados são {brasileirao[0:5]}')
print(f'Os ultimos quatro colocados são {brasileirao[-4:]}')
print(f'A listam em ordem alfabetica é {sorted(brasileirao)}')
print(f'O Goiás está na posição {goias}')
