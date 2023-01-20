# def dobra(lista):
#     pos = 0
#     while pos < len(lista):
#         lista[pos] *= 2
#         pos += 1


# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)


# def soma(* valores):
#     s = 0
#     for num in valores:
#         s += num
#     print(f'Somando os valores {valores} temos {s}')


# soma(5, 2)
# soma(2, 9, 4)

def area(larg, comp):
    a = larg*comp
    print(f'A area do terreno de {larg}x{comp} é de {a}m²')


l = float(input('Digite a largura em metros: '))
c = float(input('Digite o comprimento em metros: '))
area(l, c)
