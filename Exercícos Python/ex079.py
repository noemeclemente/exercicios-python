lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? '))
    if r in 'Nn':
        break
for i, v in enumerate(lista): # para percorrer a lista
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímapares é {impares}')
