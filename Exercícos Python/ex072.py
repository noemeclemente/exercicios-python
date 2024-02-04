# análise de dados em uma tupla
n = (int(input('Digite um número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite o último núemro: ')))

print(n)
print(f'O número novo apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O primeiro número 3 foi encontrado na posição {n.index(3)+1}')
else:
    print('O valor 3 não foi encontrado em nenhuma posição')
print('Os valores pares digitados foram ', end=' ')
for num in n:
    if num % 2 == 0:
        print(num, end=' ') # ao adicionar um end, os prints se juntam 

