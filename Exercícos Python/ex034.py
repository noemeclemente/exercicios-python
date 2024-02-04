# conversor de bases numéricas

num = int(input("Digite um número inteiro: "))
print(''' Escolha uma das bases para conversãp: 
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
opcao = int(input("Sua opção: "))
if opcao == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num) [2:]))
elif opcao == 2:
    print("{} convertido para OCTAL é igual a {}".format(num, oct(num) [2:]))
elif opcao == 3:
    print("{} convertido para HEXADECIMAL é igal a {}".format(num, hex(num) [2:]))
else:
    print("Digite uma opção válida")