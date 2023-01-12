repeat = int(
    input('Digite quantos elementos da sequencia de fibonaacci quer ver: '))

n1 = 0
n2 = 1

while repeat != 0:
    fib = n1 + n2
    n1 = n2
    n2 = fib
    repeat -= 1
    print(fib)
