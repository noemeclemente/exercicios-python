# validando entrada de dados
'''
def leiaInt(msg): # cria um função que recebe uma mensagem
    ok = False # vai verificar se a entrada do usuário é válida
    valor  = 0 # vai armazenar o valor inserido pelo usuário
    while True: # cria um loop para ver se o valor inserido é um número
        n = str(input(msg)) # recebe a entrada do usuário conevrtida para string
        if n.isnumeric(): # verifica se é um valor numérico
            valor = int(n) # valor vai ser convertido para inteiro e armazenado na variável
            ok = True # o ok passa a ser verdade, pois o valor é numérico
        else:
            print('Erro, digite um número válido! ')
        if ok: # se o valor dou um número, o programa é encerrado
            break
    return valor # retorna o valor convertido da entrada do usuário


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}') '''
def leiaInt():
    n = str(input('Digite um número: '))
    while not n.isnumeric():
        print('Ops! Apenas números são aceitos!')
        n = str(input('Digite um número: '))
    if n.isnumeric():
        n = int(n)
        print(f'Você digitou o número: {n} ')
leiaInt()