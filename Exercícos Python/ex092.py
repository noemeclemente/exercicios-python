# aprimorando os dicionários ex 95v VOLTAR NELE!!!!
time = list()
jogador = dict()
quantidade = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou?: '))
    quantidade.clear()
    for c in range(0, tot):
        quantidade.append(int(input(f'  Quantos gols na partida {c +1}')))
    jogador['gols'] = quantidade[:]
    jogador['total'] = sum(quantidade)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? (S/N): ')).upper()[0]
        if resp in 'SN':
            break
        print('Responda apenas com S ou N')
    if resp == 'N':
        break
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', ed=' ')
    for d in v.values:
        print(f'{str(d):<15}', end=' ')
    print()

print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
