km = int(input('Digite uma distancia em KM: '))

if km <= 200:
    print(f'O preço da passagem será R${km*0.5}')
else:
    print(f'O preço da passagem será R${km*0.45}')
