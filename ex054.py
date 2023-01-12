import datetime
list = [int(x) for x in input(
    'Digite o ano de nascimento de 7 pessoas diferentes: ').split()]

today = datetime.date.today()
year = today.year

x = 0
for i in list:
    idade = year - i
    if idade < 18:
        x = x + 1
print(f'{x} são menores de idade')
