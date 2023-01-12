vel = int(input('Digite a velocidade de um carro: '))

multa = (vel-80)*7

if vel <= 80:
    print('Você não foi multado')
else:
    print(f'Você foi multado em R${multa}')
