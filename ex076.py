lista = ('Pão', 1, 'Leite', 3.50, 'Frango', 10.90)

for x in range(0, len(lista), 2):
    print(f'{lista[x]} ==== R${lista[x+1]}')
