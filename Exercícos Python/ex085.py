# palpites para a mega sena
from random import randint
lista = list()
jogadas = list()
quant = int(input('Quantas vezes você quer jogar?'))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    jogadas.append(lista[:])
    lista.clear()
    tot += 1

for i, l in enumerate(jogadas):
    print(f'Jogo {i+1}:{l}')
