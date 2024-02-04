
'''import bisect
valores = list()

for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    index = bisect.bisect_right(valores, valor)
    valores.insert(index, valor)
    print(f'O número foi adicionado na poisção {index}')

print(f'Os números adicionados foram {valores}')'''

lista = []
for c in range(5):
    valor = int(input('Digite um valor: '))
    if c == 0:
        lista.append(valor)
    elif valor > lista[-1]:
        lista.append(valor)
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')




