from random import randint
from time import sleep

#apresentando game
score = 0
print('\033[1;37;46m=\033[m'*148)
print('')
print('')
print(f'\033[1;33m{"TEXUGA_____GAMES 🍯":*^147}\033[m')
print('                                                                   \033[1;36m APRESENTA\033[m')
print('                                                                 \033[1;33m JO \033[m \033[1;31m '
      'KEN \033[m \033[1;35m PÔ \033[m')
print('\033[1;37;46m=\033[m'*148)

#introdução
print('''\033[1;36mNesse Game divertido você será convidado por MK para um desafio de jokenpo em busca da GLÓRIA.
 Você terá apenas 3 chances para escolher entre "Pedra", "Papel" e "Tesoura e cada rodada
 valerá 10 pontos. Será que você consegue combater MK
e chegar até o final?.\033[m''')

#inicio gameplay
print(f'{"PRIMEIRA RODADA":=^60}')
inicio = str(input('\033[0;33m E ai, Vai encarar? s/n \033[m'))
if inicio.lower() == 's':
    print('\033[1;33m LET´S GO!')
    print('Você primeiro...\033[m')
elif inicio == 'n':
    print('\033[0;37mBem, quem sabe na proxíma.\033[m')
    quit()
elif inicio != 's' != 'n':
    print('\033[1;31mComando Inválido. Tente novamente.\033[m')

lista = ('Pedra', 'Papel','Tesoura')
print('\033[1;36mSuas opções são \n [0] Pedra \n [1] Papel \n [2] Tesoura\033[m')
player = int(input('\033[1;33mQual você escolhe?\033[m '))
if player !=0 and player != 1 and player != 2:
     print('Opção Inválida')
mk = randint(0,2)
print('\033[1;33m JO\033[m')
sleep(1)
print('\033[1;31m KEN \033[m')
sleep(1)
print('\033[1;35m PÔ\033[m')

print(f'\033[1;36mVocê escolheu {lista[player]}\033[m')
print(f'\033[1;31mMK escolheu {lista[mk]}\033[m')

#condições


if mk == 0:
    if player == 0:
        print('\033[1;33m Temos um empate. Proxíma rodada.\033[m')
    elif player == 1:
        score = score + 10
        print('\033[1;32m Você venceu a vez. Proxíma rodada.\033[m')
    elif player == 2:
        print('\033[1;34m MK venceu a vez. Proxíma rodada. \033[m')
    else:
        print('')
if mk == 1:
    if player == 1:
        print('\033[1;33m Temos um empate. Proxíma rodada.\033[m')
    elif player == 0:
        print('\033[1;34m MK venceu a vez. Proxíma rodada.\033[m')
    elif player == 2:
        score = score + 10
        print('\033[1;32m Você venceu a vez. Proxíma rodada.\033[m')
    else:
        print('')
if mk == 2:
    if player == 2:
        print('\033[1;33m Temos um empate. Proxíma rodada.\033[m')
    elif player == 0:
        score = score + 10
        print('\033[1;32m Você venceu a vez. Proxíma rodada.\33[m')
    elif player == 1:
        print('\033[1;34m MK venceu a vez. Proxíma rodada.\033[m')
    else:
        print('')

#rodada 2
print(f'{"SEGUNDA RODADA":=^60}')
print('')
print('\033[1;36mSuas opções são \n [0] Pedra \n [1] Papel \n [2] Tesoura\033[m')
player = int(input('\033[1;33mQual você escolhe?\033[m '))
if player !=0 and player != 1 and player != 2:
     print('Opção Inválida')
mk = randint(0,2)
print('\033[1;33m JO\033[m')
sleep(1)
print('\033[1;31m KEN \033[m')
sleep(1)
print('\033[1;35m PÔ\033[m')

print(f'\033[1;36mVocê escolheu {lista[player]}\033[m')
print(f'\033[1;31mMK escolheu {lista[mk]}\033[m')

#condições


if mk == 0:
    if player == 0:
        print('\033[1;33m Temos um empate. Proxíma rodada.\033[m')
    elif player == 1:
        score = score + 10
        print('\033[1;32m Você venceu a vez. Proxíma rodada.\033[m')
    elif player == 2:
        print('\033[1;34m MK venceu a vez. Proxíma rodada. \033[m')
    else:
        print('')
if mk == 1:
    if player == 1:
        print('\033[1;33m Temos um empate. Proxíma rodada.\033[m')
    elif player == 0:
        print('\033[1;34m MK venceu a vez. Proxíma rodada.\033[m')
    elif player == 2:
        score = score + 10
        print('\033[1;32m Você venceu a vez. Proxíma rodada.\033[m')
    else:
        print('')
if mk == 2:
    if player == 2:
        print('\033[1;33m Temos um empate. Proxíma rodada.\033[m')
    elif player == 0:
        score = score + 10
        print('\033[1;32m Você venceu a vez. Proxíma rodada.\33[m')
    elif player == 1:
        print('\033[1;34m MK venceu a vez. Proxíma rodada.\033[m')
    else:
        print('')

#rodada3
print(f'{"ÚLTIMA RODADA":=^60}')
print('\033[1;36mSuas opções são \n [0] Pedra \n [1] Papel \n [2] Tesoura\033[m')
player = int(input('\033[1;33mQual você escolhe?\033[m '))
if player !=0 and player != 1 and player != 2:
     print('Opção Inválida')
mk = randint(0,2)
print('\033[1;33m JO\033[m')
sleep(1)
print('\033[1;31m KEN \033[m')
sleep(1)
print('\033[1;35m PÔ\033[m')

print(f'\033[1;36mVocê escolheu {lista[player]}\033[m')
print(f'\033[1;31mMK escolheu {lista[mk]}\033[m')

#condições


if mk == 0:
    if player == 0:
        print('\033[1;33m Temos um empate.\033[m')
    elif player == 1:
        score = score + 10
        print('\033[1;32m Você venceu a vez.\033[m')
    elif player == 2:
        print('\033[1;34m MK venceu a vez. \033[m')
    else:
        print('')
if mk == 1:
    if player == 1:
        print('\033[1;33m Temos um empate.\033[m')
    elif player == 0:
        print('\033[1;34m MK venceu a vez.\033[m')
    elif player == 2:
        score = score + 10
        print('\033[1;32m Você venceu a vez.\033[m')
    else:
        print('')
if mk == 2:
    if player == 2:
        print('\033[1;33m Temos um empate.\033[m')
    elif player == 0:
        score = score + 10
        print('\033[1;32m Você venceu a vez.\33[m')
    elif player == 1:
        print('\033[1;34m MK venceu a vez.\033[m')
    else:
        print('')
print(f'\033[1;34m Sua pontuação final foi {score} \033[m')

