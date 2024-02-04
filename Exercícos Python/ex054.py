# validaçõa de dados

sexo = str(input("Sexo [F/M]: ")).strip().upper()[0] # exibe apenas a primeira letra
while sexo not in 'MnFf':
    sexo = str(input("Dados inválidos, digite novamente: ")).strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))
