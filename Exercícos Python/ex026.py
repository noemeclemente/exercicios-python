# radar eletrônico

vel = float(input("Qual a velocidade do carro?"))
if vel > 80:
    print("MULTADO! Você excedeu o limite de velocidade permitido")
    multa = (vel - 80) * 7
    print("O valor da multa a ser pago é de {:.2f}".format(multa))
print("Tenha um bom dia, dirija com segurança!")