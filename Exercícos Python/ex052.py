# maior e menor da sequência
''' pesos = []
for pess in range(1, 6):
    peso = float(input("Peso da {}ª pessoa: ".format(pess)))
    pesos.append(peso)
maior = max(pesos)
menor = min(pesos)
print("O maior peso analisado é {}, e o menor peso analisado é {}".format(maior, menor)) '''

# solução do guanabara
maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input("Digite o peso da {}ª pessoa: ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {}Kg, e o menor peso lido foi de {}Kg".format(maior,menor))
