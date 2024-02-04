# alistamento militar

from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc
sexo = str(input("Qual é o seu sexo? MASC/FEM: ").upper())

if sexo == "MASC":
    print("Quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))
if sexo == "FEM":
    print("Mulheres não precisam se alistar")

if idade == 18 and sexo == "MASC":
    print("Você tem que se alistar imediatamente!")
elif idade < 18 and sexo == "MASC":
    saldo = 18 - idade
    print("Você ainda não tem idade para se alistar. Ainda faltam {} anos para o seu alistamento".format(saldo))
    ano = atual + saldo
    print("Seu alistamento será em {}".format(ano))
elif idade > 18 and sexo == "MASC":
    saldo = idade - 18
    print("Você já deveria ter se alistado há {} anos.".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}".format(ano))


