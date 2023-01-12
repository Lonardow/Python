import random

alunos = input('Digite o nome de 4 alunos para sortear 1: ').split()

escolhido = random.choice(alunos)

print(f"O escolhido foi {alunos[random.randint(0,3)]}")

print(f"O aluno escolhido foi {escolhido}")
