# função de contador
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} a {f} de {p} em {p}')
    sleep(1)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.3)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.3)
            cont -= p
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:'))
contador(ini, fim, passo)