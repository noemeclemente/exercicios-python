# aprovando empréstimo

valor = float(input("Valor da casa: "))
salario = float(input("Salário: "))
anos = int(input("Em quantos anos vai pagar: "))
prestacao = valor / (anos * 12)
print("Para pagar uma casa de {:.2f} em {:.2f} anos.".format(valor, anos), end = '')
print("A prestação será de {:.2f}".format(prestacao))
if prestacao > salario * 30 / 100:
    print("Empréstimo negado")
else:
    print("Empréstimo concedidio ")