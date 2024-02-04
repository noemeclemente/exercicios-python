# extraindo dados de uma lista

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar? (S/N):'))
    if r in 'Nn':
        break

lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O cinco faz parte da lista')
else:
    print('O número 5 não foi encontrado')

