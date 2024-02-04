# mais sobre matriz em python
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0 # soma dos números pares, maior valor da segunda linha e soma dos valores da terceira coluna
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para as posições [{l}, {c}:]'))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end=' ')
        if matriz[l] [c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma de todos os números pares é de {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
print(f'O maior número da segunda linha é {max(matriz[1])}')