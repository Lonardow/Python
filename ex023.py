number = int(input('digite um numero de 0 a 9999: '))

milhar = number//1000
centena = (number//100) % 10
dezena = (number % 100)//10
unidade = (number % 10)

print(milhar)
print(centena)
print(dezena)
print(unidade)
