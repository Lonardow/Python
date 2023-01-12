#  Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

nome = input('Digite seu nome completo: ')

upper = nome.upper()
print(upper)
lower = nome.lower()
print(lower)
trueSize = nome.split()
trueSize = ''.join(trueSize)
print(len(trueSize))
firstNameSize = nome.split()
firstNameSize = firstNameSize[1]
print(len(firstNameSize))
