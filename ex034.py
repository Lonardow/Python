salario = float(input('Digite seu salário para calcular o aumento: '))

if salario > 1250:
    print(
        f'Com o aumento de 10% seu salário ficará R${salario+(salario*(10/100))}')
else:
    print(
        f'Com o aumento de 15% seu salário ficara R${salario+(salario*(15/100))}')
