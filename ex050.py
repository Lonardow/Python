list = [int(x) for x in input('Digite 6 numeros inteiros: ').split()]
y = 0
for x in list:
    if x % 2 == 0:
        y = y+x
print(y)
