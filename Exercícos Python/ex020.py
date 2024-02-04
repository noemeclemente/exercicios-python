# separando dígitos de um número

''' num = int(input("Informe um número:"))
n = str(num)
print("Analisando o número {}".format(num))
print("Unidade: {}".format(n[3]))
print("A dezena é {}".format(n[2]))
print("A centena é {}".format(n[1]))
print("Milhar {}".format(n[0])) '''

num = int(input("Informe um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Analisando o número: {}".format(num))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {} ".format(m))

''' Pra ele descobrir a centena ele faz isso:
Faz a divisão inteira por 100: 1234 // 100 = 12
Depois pega o resultado e dividi por 10, mas pega só o resto dessa divisão (que é o módulo): 12 % 10 = 2
Ou seja, a centena é 2.'''