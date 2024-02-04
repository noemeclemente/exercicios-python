# classificando atletas

from datetime import date
ano = int(input("Em que ano você nasceu?: "))
hoje = date.today().year
idade = hoje - ano
print("Você tem {} anos e ".format(idade))
if idade <= 9:
    print("Sua categoria é mirim")
elif idade <= 14:
    print("Sa categoria é infantil")
elif idade <= 19:
    print("Sua categoria é junior")
elif idade <= 25:
    print("Sa categoria é senior")
else:
    print("Sua categoria é master")



