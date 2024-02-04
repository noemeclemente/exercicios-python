# progressão aritmética v.2

primeiro = int(input('Primeiro termo: '))
r = int(input("Razão da PA: "))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end=' ')
    termo += r
    cont += 1
print('FIM')