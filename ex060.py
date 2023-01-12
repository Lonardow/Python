num = int(input('Digite um numero para ver seu fatorial: '))
fat = num
while num != 1:
    num = num-1
    fat = fat * num
print(fat)
