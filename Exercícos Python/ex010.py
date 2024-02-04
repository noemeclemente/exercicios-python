# calculando descontos

preco = float(input("Qual é o valor do produto que você deseja comprar: "))
pagamento = input("De que maneira deseja pagar, a vista (1), ou parecelado (2)?")

if pagamento == '1':
    print("O valor do seu produto é de {} reais, pagando a vista você ganhará um desconto de 10% e pagará {} reais".format(preco, preco - (preco*10/100)))
elif pagamento == '2':
    print(" O valor do seu produto é {}, pagando parcelado você terá juros de 8%, resultando em {} reais".format(preco, preco + (preco *8/100)))
else :
    print("Digite uma opção válida")
