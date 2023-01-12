preco = float(input('Qual o preço do produto? '))
desc = int(input('Qual o desconto do produto? '))

print(
    f'O desconto é de R${preco*(desc/100)}, e o valor com desconto será R${preco-desc} ')
