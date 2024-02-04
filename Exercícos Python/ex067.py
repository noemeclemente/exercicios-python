total = totproduto = barato = 0
nomebarato: ' '
cont = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: '))
    total += preço
    cont += 1
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if preço > 1000:
        totproduto += 1
    if cont == 1:
        barato = preço
        nomebarato = produto
    else:
        if preço < barato:
            barato = preço
            nomebarato = produto
    if continuar == 'N':
        break
print(f'O total de compras foi de {total}')
print(f'Temos {totproduto} produtos custando mais de R$1.000')
print(f'O produto mais barato foi {nomebarato} que custa {barato}')
print('{:-^40}'.format('FIM DO PROGRAMA'))