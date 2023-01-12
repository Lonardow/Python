x = 0

while True:
    count = 1
    val = int(input('Quer ver a tabuada de qual valor? '))
    if val < 0:
        break
    print('-'*20)
    while count <= 10:
        mult = val * count
        print(f'{val} x {count} = {mult}')
        count += 1
    print('-'*20)
print('tabuada encerrada')
