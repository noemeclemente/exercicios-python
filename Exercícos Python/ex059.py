# super progressão aritmética

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    while cont <= 10:
        total = total + mais
        print('{} - '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print('FIM')
print('Você buscou {} termos no total'.format(cont)) 