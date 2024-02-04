# maior e menor valores na lista

lista = []
for v in range(0, 5):
    lista.append(int(input(f'Digite um valor na poisção {v}: ')))

    maior = max(lista)
    menor = min(lista)

print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end=' ')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end=' ')
print(f'O menor valor digitado foi {min(lista)} nas posições ', end=' ')
for indice, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{indice}...', end=' ')
        
