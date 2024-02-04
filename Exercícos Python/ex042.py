# game pedra papel e tesoura

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogada = int(input("Qual vai ser a sua jogada?: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)
print("-=" * 10)
print("O computador escolheu {}".format(itens[computador]))
print("O jogador escolheu {}".format(itens[jogada]))
print("-=" * 10)

if computador == 0:
    if jogada == 0:
        print("EMPATE")
    elif jogada == 1:
        print("Você venceu")
    elif jogada == 2:
        print("Você perdeu")
    else:
        print("Jogada inválida")
elif computador == 1:
    if jogada == 0:
        print("VOCÊ PERDEU")
    elif jogada == 1:
        print("EMPATE")
    elif jogada == 2:
        print("VOCÊ VENCEU")
    else:
        print("Jogada inválida")
elif computador == 2:
    if jogada == 0:
        print("VOCÊ VENCEU")
    if jogada == 1:
        print("VOCÊ PERDEU")
    if jogada == 2:
        print("EMPATE")
    else:"Jogada inválida"
