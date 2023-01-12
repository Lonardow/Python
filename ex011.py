x, y = [float(x) for x in input(
    'Digite a altura e a largura da parede respectivamente: ').split()]

area = x * y

print(f"serão necessarios {area/2} litros de tinta para pintar a parede")
