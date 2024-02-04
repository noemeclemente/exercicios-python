# aluguel de carros

km = float(input("Quantos quilômetros foram rodados: "))
d = int(input("Por quantos dias ele foi alugado: "))
preco = (km * 0.15) + (d * 60)

print(" O preço a pagar é de {:.2f}".format(preco))