
n = int(input('Digite um número [999 para parar]: '))
c = 0
soma = 0
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))
print('A soma de todos os {} valores digitados é de {}'.format(c, soma))