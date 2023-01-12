aluno = dict()

aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Media'] = float(input('Digite a media dele: '))
if aluno['Media'] < 5:
    aluno['Situacao'] = 'Reprovado'
elif aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
else:
    aluno['Situacao'] = 'em Recuperação'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')


# print(f'O nome do aluno é {aluno["nome"]}')
# print(f'A média dele foi {aluno["media"]}')
# print(f'{aluno["nome"]} está {aluno["situacao"]}')
