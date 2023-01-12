import random
alunos = input('Digite o nome de 4 alunos').split()

random.shuffle(alunos)

print(f'A ordem de apresentação será {alunos}')
