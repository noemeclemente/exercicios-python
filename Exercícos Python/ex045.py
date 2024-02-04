# soma ímpares múltiplos de três
'''cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print("A soma de {} número solicitados é igual a {}".format(cont, soma)) '''

# programa que calcula todos os números ímpares divisíveis por 9 entre 1 a 300
soma = 0
cont = 0
for n in range(1,301,2):
    if n % 9 == 0:
        cont += 1
        soma += n
print("A soma de todos os {} valores solicitados é de {}".format(cont,soma))
