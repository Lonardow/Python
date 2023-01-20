aprov = dict()
grupo = list()
gols = list()

while True:
    aprov['nome'] = str(input('Digite o nome do jogador: '))
    part = int(input('Quantas partidas ele jogou? '))
    for i in range(part):
        gols.append(int(input(f'Quantos gols ele fez na partida {i+1}? ')))

    aprov['gols'] = gols[:]
    aprov['total'] = sum(gols)
    grupo.append(aprov.copy())
    cont = str(input('Quer continuar? '))
    if cont in 'Nn':
        break
    gols.clear()
print(grupo)

print(f'cod   nome', ' '*8, 'gols', ' '*8, 'total')
print('-'*50)
for x, y in enumerate(grupo):
    print(
        f'{x} {grupo[x]["nome"]}     {grupo[x]["gols"]}    {grupo[x]["total"]}')
print('-'*50)
while True:
    data = int(input('Mostrar dados de qual jogador? '))
    if data == 999:
        break
    elif data > len(grupo)-1:
        print(f'ERRO! Não existe jogador com codigo {data}')
        print('-'*50)
    else:
        print(f'LEVANTAMENTO DO JOGADOR {grupo[data]["nome"]}: ')
        for x, y in enumerate(grupo[data]['gols']):
            print(f'No jogo {x} fez {y} gols.')
