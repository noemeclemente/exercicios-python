# tuplas com times de futebol

times = ('Bragantino', 'Athletico-PR', 'Fortaleza', 'Palmeiras',
         'Atlético-GO', 'Atlético-MG', 'Flamengo', 'Fluminense',
         'Bahia', 'Santos', 'Cotinthians', 'Ceará SC', 'Internacional',
         'Juventude', 'Sport Recife', 'Cuiabá', 'Chapecoense', 'São Paulo',
         'América-MG', 'Grêmio')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros colocados são{times[0:5]}')
print(f'Os últimos 4 colocados {times[-4:]}')
print('Em ordem alfabética:', tuple(sorted(times)))
print(f'A posição do time chapecoense é {times.index("Chapecoense")+1}')