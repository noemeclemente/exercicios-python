# um print especial
def escreva(msg):
    tam = len(msg) + 4
    print('~'* tam)
    print(f'  {msg}')
    print('~' * tam)


escreva('Oi')
escreva('Curso de python')