import datetime
import time

ano = datetime.date.today().year


def canvote(nasc):
    idade = ano - nasc
    if idade < 16:
        return print(f'Com {idade}, NAO PODE VOTAR')
    elif idade >= 16 and idade < 18 or idade > 65:
        return print(f'Com {idade} O VOTO É OPCIONAL')
    else:
        return print(f'Com {idade} O VOTO É OBRIGATORIO')


n = int(input(f'Em que ano você nasceu? '))
time.sleep(1)
canvote(n)
