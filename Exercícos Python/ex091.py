# unindo dicionários e listas
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro, por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]:')).upper()[0]
        if resp in 'SN':
            break
        print('Erro, digite apenas S ou N')
    if resp == 'N':
        break
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
    print()
print(f'Lista de pessoas que estão acima da média: ',end= ' ')
for p in galera:
    if p["idade"] >= média:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
