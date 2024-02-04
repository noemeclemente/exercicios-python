cont = 0
soma = 0
while True:
    n = int(input('Digite um número inteiro: '))

    if n == 999:
        break

    cont += 1
    soma += n
print('a soma de todos os {} números digitados é igual {}'.format(cont, soma))