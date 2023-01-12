import datetime

year = datetime.datetime.now().year

funcionarios = dict()

funcionarios['nome'] = str(input('Digite o nome: '))
x = int(input('Digite o ano de nascimento: '))
funcionarios['idade'] = year - x
funcionarios['ctps'] = int(
    input('Digite sua carteira de trabalho [0 se nao tiver]: '))
if funcionarios['ctps'] == 0:
    del funcionarios['ctps']
else:
    funcionarios['Ano de Contrat'] = int(
        input('Digite o ano em que foi contratado: '))
    funcionarios['salario'] = int(input('Digite seu salario: '))
    aposent = (funcionarios['Ano de Contrat'] + 35) - x
    funcionarios['Aposentad'] = aposent
print(funcionarios)

for k, v in funcionarios.items():
    print(f'{k} tem o valor {v}')
