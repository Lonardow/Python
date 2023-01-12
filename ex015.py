km, dias = [float(km) for km in input(
    'Informe a quilometragem rodada e a quantidade de dias que ficou com o carro:  ').split()]

valDia = dias*60
valRod = 0.15*km

print(f'O custo do aluguem do carro foi R${valDia+valRod}')
