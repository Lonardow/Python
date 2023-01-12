sexo = ''
sexo = input('Digite o seu sexo [M/F]: ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Digite o seu sexo [M/F]: ')
print(f'sexo {sexo} registrado com sucesso')
