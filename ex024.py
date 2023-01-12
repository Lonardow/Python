cidade = input('Digite o nome de uma cidade: ')
cidade = cidade.lower()

cidade = cidade.split()

isSanto = 'santo' in cidade[0]

print(isSanto)
