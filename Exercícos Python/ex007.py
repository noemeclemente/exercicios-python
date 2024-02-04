# Calculando descontos

preco = float(input("Qual é o preço do produto? R$"))
novo = preco - preco*5/100
print("O novo preço com desconto é de {:.2f}R$".format(novo))