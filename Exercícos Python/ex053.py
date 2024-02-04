# analisador completo
somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
menormulheres = 0
for p in range(1, 5):
    print("----- {}ª PESSOA -----".format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [F/M]: ")).upper()
    somaidade += idade # recebe todas as idades
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        menormulheres += 1


mediaidade = somaidade / 4
print("A média de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho se chama {} e tem {} anos de idade".format(nomevelho, maioridade))
print("A quantidade de mulheres menores de 20 anos é de {}".format(menormulheres))
