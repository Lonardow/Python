x = list(str(input('Digite uma expressão matematica: ')))

parent = []

for item in x:
    if item == '(':
        parent.append('(')
    elif item == ')':
        if len(parent) > 0:
            parent.pop()
        else:
            parent.append
            break
if len(parent) > 0:
    print('Essa expressão esta errada')
else:
    print('Essa expressão esta correta')
