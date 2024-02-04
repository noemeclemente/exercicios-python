# sistema interativo de ajuda em python
from time import sleep
c = ('\033[m',       # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[0;30;47m'    # branco
     )

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6], end='')
    help(com)
    print(c[0],end='')
    sleep(0.3)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')



comando = ''
while True:
    título('BEM VINDO AO SISTEMA DE AJUDAS PyHelp', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)

