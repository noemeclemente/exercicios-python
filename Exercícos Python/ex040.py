# analisando índice massa corporal

peso = float(input("Qual é o seu peso (Kg): "))
altura = float(input("Qual é a sua altura? "))
imc = peso / (altura ** 2)
print("O IMC dessa pessoa é {:.1f}".format(imc))
if imc <= 18.5:
    print("Você está abaixo do peso")
elif imc <= 24.9:
    print("você está no peso ideal")
elif imc <= 29.9:
    print('Você está com sobrepeso')
elif imc <= 34.9:
    print("Você está com obesidade Grau I")
elif imc <= 39.9:
    print("Você está com obesidade Grau II")
else:
    print("Você está com obesidade Grau III")

