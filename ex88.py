import random
import time

j = int(input('Quantos jogos quer que eu sorteie? '))

for quant in range(0, j):
    jogo = []
    while len(jogo) < 6:
        x = (random.randint(1, 60))
        if x not in jogo:
            jogo.append(x)
    jogo.sort()
    time.sleep(0.5)
    print(f"Jogo {quant+1}: {jogo}")
