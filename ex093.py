aprov = dict()
gols = []
soma = 0

aprov['nome'] = str(input('Digite o nome do jogador: '))
part = int(input('Quantas partidas ele jogou? '))
for i in range(part):
    gols.append(int(input(f'Quantos gols ele fez na partida {i+1}? ')))

aprov['gols'] = gols
aprov['total'] = sum(gols)
for k, v in aprov.items():
    print(f'o campo {k} tem o valor {v}')

print(f'O jogador {aprov["nome"]} jogou {part} partida(s).')
for x, y in enumerate(gols):
    print(f'=> Na partida {x+1}, fez {y} gols.')
print(f'Um total de {sum(gols)} gols')
