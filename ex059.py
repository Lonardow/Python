
from time import sleep
val1 = int(input('Digite um valor: '))
val2 = int(input('Digite outro valor: '))
choice = 0

while choice != 5:
    print(
        '\n[1] Somar\n[2] Multiplicar\n[3] Subrair\n[4] Novos numeros\n[5] Sair do programa')
    choice = int(input('Digite um numero para a função que deseja: '))

    if choice == 1:
        result = val1 + val2
        print('O resultado da soma foi ', result)

    elif choice == 2:
        result = val1 * val2
        print('O resultado da multiplicação foi ', result)
    elif choice == 3:
        result = val1 - val2
        print('O resultado da subtração é ', abs(result))
    elif choice == 4:
        val1 = int(input('Digite um valor: '))
        val2 = int(input('Digite outro valor: '))
    elif choice == 5:
        print('Finalizando')
    else:
        print('opção invalida')
    print('=-='*8)
    sleep(1)
print('Fim do programa')
