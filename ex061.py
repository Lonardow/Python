num = int(input('Digite o primeiro: '))
raz = int(input('Razao da PA: '))

c = 10
x = 0
while c != 0:
    x = x+1
    print(num)
    num = num + raz
    c = c-1
    if c == 0:
        print('pausa')
        c = int(input('Quantos termos quer mostrar a mais? '))
        print(f'A progressão foi finalizada com {x} termos mostrados')
