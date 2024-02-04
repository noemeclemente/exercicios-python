from random import randint

vitoria = 0

while True:
    jogador = int(input('Digite um número para jogar: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par (P) ou Ímpar (I): ')).strip().upper()

    print(f'Você jogou {jogador} e o computador jogou {computador}, o total foi {total}')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu')
            vitoria += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 != 1 :
            print('Você venceu')
            vitoria += 1
        else:
            print('Você perdeu')
            break

print(f'Total de vitórias: {vitoria}')
