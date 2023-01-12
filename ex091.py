import random
import operator

jogadores = dict()
# comida = {'cafe': 14, 'arroz': 3}
for j in range(0, 4):
    jogadores[f'Jogador{j+1}'] = random.randint(0, 100)

ranking = dict()

print(jogadores)
for k, v in jogadores.items():
    print(f'{k} sorteou {v}')

ranking = sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True)
for i, x in enumerate(ranking):
    print(f'O {i+1}º lugar foi o {x[0]} com {x[1]}')
