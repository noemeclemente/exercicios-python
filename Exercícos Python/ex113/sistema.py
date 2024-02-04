from ex113.lib.interface import *
from time import sleep
from ex113.lib.arquivo import *

arq = ('cursoemvideo.txt')
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Opção 3')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)
