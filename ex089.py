# temp = []
# alunos = []
# notas = []
# while True:
#     temp.append(str(input('Digite o nome do aluno: ')))
#     notas.append(float(input('Nota 1: ')))
#     notas.append(float(input('Nota 2: ')))
#     media = (notas[0] + notas[1]) / 2
#     temp.append(notas[:])
#     temp.append(media)
#     alunos.append(temp[:])
#     temp.clear()
#     notas.clear()
#     x = str(input('Deseja continuar? [S/N] '))
#     if x in 'Nn':
#         break
# print(alunos)
# for i in range(0, len(alunos)):
#     print(f'Aluno {alunos[i][0]} média {alunos[i][2]}')


boletim = list()

while True:
    nome = str(input('Digite o nome do aluno: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])
    x = str(input('Deseja continuar? [S/N] '))
    if x in 'Nn':
        break

for i in range(0, len(boletim)):
    print(f'Aluno {boletim[i][0]} média {boletim[i][2]}')
