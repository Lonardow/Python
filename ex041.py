import datetime
nasc = int(input('Digite o ano de nascimento do atleta: '))

today = datetime.date.today()
year = today.year
idade = year-nasc

print(idade)

if idade <= 9:
    print('Mirim')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade == 20:
    print('Senior')
elif idade > 20:
    print('Master')
