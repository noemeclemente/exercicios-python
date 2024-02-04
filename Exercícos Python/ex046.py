# tabuada versão 2

n = int(input("Digite m número para ver sua tabuada: "))

for c in range (1, 11, 1):
    print("{} X {} = {}".format(n, c, n*c))
