pesos = [int(x) for x in input(
    'Digite 5 pesos diferentes para saber o maior e o menor: ').split()]

print(pesos)
maior = 0
menor = pesos[0]
for c in pesos:
    if c > maior:
        maior = c
    if menor > c:
        menor = c

print('maior', maior)
print('menor', menor)
