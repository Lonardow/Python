import math
cat1, cat2 = [float(cat1) for cat1 in input(
    'Digite o comprimento do cat1 e do cat 2: ').split()]

print(f'O comprimento da hipotenusa é {math.hypot(cat1,cat2):.2f}')
