# aumentos múltiplos

salario = float(input("Qual é o salário atual? "))
if salario > 1250:
    atual = (salario * 10 / 100) + salario
    print("Seu salário atual é de {:.2f}".format(atual))
else:
    atual = (salario * 15 / 100) + salario
    print("O salário atal é de {:.2f}".format(atual))