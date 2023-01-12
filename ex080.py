lista = []
maior = menor = 0

for cont in range(0, 5):
    x = int(input('Digite um valor: '))
    if cont == 0 or x > lista[-1]:
        lista.append(x)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if x <= lista[pos]:
                lista.insert(pos, x)
                print(f'adicionado na posição {pos} da lista.')
                break
            pos += 1
