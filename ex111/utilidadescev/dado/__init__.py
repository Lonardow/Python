
def leiaDinheiro(x):
    valid = False
    while not valid:
        inp = str(input(x)).replace(',', '.').strip()
        if inp.isalpha() or inp == '':
            print(f'\033[0;031mERRO: \"{x}\" é um preço inválido!\033[m')
        else:
            valid = True
            return float(inp)
