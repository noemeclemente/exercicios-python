# cadastro de jogador em python
jogador = dict()
quantidade = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou?: '))
for c in range(0, tot):
    quantidade.append(int(input(f'  Quantos gols na partida {c +1}')))
jogador['gols'] = quantidade[:]
jogador['total'] = sum(quantidade)
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
