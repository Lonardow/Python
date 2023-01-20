pessoa = dict()
grupo = list()
soma = 0
while True:
    pessoa['nome'] = str(input('Digite o nome: '))
    pessoa['sexo'] = str(input('Digite o sexo: M/F '))
    pessoa['idade'] = int(input('Digite a idade: '))
    grupo.append(pessoa.copy())
    x = str(input('Quer continuar? [S/N] '))
    if x in 'Nn':
        break
quant = len(grupo)

for i, o in enumerate(grupo):
    soma += grupo[i]['idade']
media = soma/quant


print(f'O grupo tem {quant} pessoas')
print(f'A média de idade das pessoas é {media:.1f}')
print(f'As mulheres cadastradas foram: ', end='')
for i, o in enumerate(grupo):
    if grupo[i]["sexo"] in 'Ff':
        print(f'{grupo[i]["nome"]}', end=' ')
print(f'Lista de pessoas com idade acima da média: \n', end='')
for a, b in enumerate(grupo):
    if a > 0:
        print()
    if grupo[a]["idade"] > media:
        for k, v in grupo[a].items():
            print(f'{k} = {v}', end=' ')
