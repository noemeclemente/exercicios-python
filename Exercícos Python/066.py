# análise de dados do grupo
maiores = 0
homens = 0
mulheres = 0
while True:
    print('cadastre uma pessoa')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo= str(input('Sexo: [F/M]')).strip().upper()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if sexo == 'M':
        homens += 1
    if continuar == 'N':
            break
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todos temos {homens} homen(s)')
print(f'E temos {mulheres} mulheres com menos de 20 anos')


# fazer um cógigo de cadastramento de código onde o usuário vai cadastrando até digitar a letra n