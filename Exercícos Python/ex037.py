# calculando média
n1 = float(input("Primeira nota: "))
n2 = float(input("Segnda nota: "))
media = (n1 + n2) / 2
print("Tirando {} e {}, a média do aluno é {}".format(n1, n2, media))
if media >= 7:
    print("O aluno esta aprovado")
elif media >= 5:
    print("O aluno está de recuperação")
else:
    print("O alno está reprovado")