import random

rand = tuple(random.randint(1, 99) for x in range(0, 5))
print(rand)
print(
    f'O menor numero da lista é {sorted(rand)[0]} maior numero é {sorted(rand)[-1]}')
