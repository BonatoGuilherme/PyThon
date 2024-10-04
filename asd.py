preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o desconto do produto: "))
precoFinal = preco *(1 - (desconto/100))

print(precoFinal)