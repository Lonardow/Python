maior = homens = mulheres = 0
while True:
    sexo = str(input('Digite seu sexo [M/F]: ')).lower()[0]
    idade = int(input('Digite sua idade: '))
    cont = str(
        input('Você deseja cadastrar outra pessoa? [S/N]: ')).strip().lower()[0]
    if idade > 18:
        maior += 1
    if sexo == 'm':
        homens += 1
    elif sexo == 'f' and idade < 20:
        mulheres += 1
    if cont == 'n':
        break
print(
    f'Foram cadastradas {maior} pessoas maiores de 18 anos\n{homens} homens e {mulheres} mulheres menores de 20 anos')
