# valores único em uma lista
números = list()
while True:
    n = int(input('Digite um número: '))
    if n not in números:
        números.append(n)
    else:
        print('Número duplicado, não vou adicionar. ')
    r = str(input('Deseja continuar? (S/N)?: '))
    if r in 'Nn':
        break
números.sort()
print(f'Os números digitados foram {números}')