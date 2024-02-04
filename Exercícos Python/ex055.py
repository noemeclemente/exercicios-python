# jogo da advinhação
''' from random import randint
computador = randint(1, 10)
tentativas = 0
print("Sou seu computador...\nAcabei de pensar em um número de 0 a 10\nConsegue advinhar qual foi? ")
palpite = int(input("Qual é o seu palpite? "))
while palpite != computador:
    if palpite > computador:
        palpite = int(input("Menos... tente novamente: "))
        tentativas += 1
    if palpite < computador:
        palpite = str(input("Mais... tente novamente: "))
        tentativas += 1
print("Parabéns, depois de {} tentativas, você acertou".format(tentativas))
print("O número sorteado foi {}".format(computador)) '''

from random import randint
computador = randint(1, 10)
print("Advinhe o número de 0 a 10 que eu pensei ")
acertou = False
tentativas = 0
while not acertou: # o comando not inverte o valor booleano
    palpite = int(input("Qual é o seu palpite?: "))
    tentativas += 1
    if palpite == computador:
        acertou = True
    else:
        if palpite < computador:
            print("Mais... tente novamente")
        elif palpite > computador:
            print("Menos... tente novamente")
print("Parabéns, depois de {} tentativas você acertou".format(tentativas))
print("O número sorteado foi {}".format(computador))
