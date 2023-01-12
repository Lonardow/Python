import datetime

nasc = int(input('QUAL O SEU ANO DE NASCIMENTO? :'))
today = datetime.date.today()
year = today.year

idade = year - nasc

canAlist = abs(idade - 18)

if idade < 18:
    print(
        f'Você tem {idade} anos e ainda faltam {canAlist} anos para voce poder se alistar')
elif idade > 18:
    print(
        f'Você tem {idade} anos já se passaram {canAlist} anos da data de se alistar')
elif idade == 18:
    print(f'Você tem {idade} anos e ja pode se alistar')
