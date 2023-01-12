peso = float(input('Qual o seu peso?: '))
altura = float(input('Qual a sua altura?: '))

imc = int(peso/(altura**2))


if imc < 18.5:
    print('Abaixo do peso')
elif 18 < imc >= 24:
    print('Peso ideal')
elif imc in range(25, 30):
    print('Sobrepeso')
elif imc in range(30, 40):
    print('Obesidade')
elif imc > 40:
    print('Obesidade morbida')
