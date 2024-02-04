# criando um menu de opções
'''v1 = int(input("Primeiro valor: "))
v2 = int(input("Segundo valor: "))
continuar = True
print([ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior 
[ 4 ] novos números 
[ 5 ] sair do programa)

while True:
    escolha = int(input('Qual operação deseja realizar?:'))
    if escolha == 1:
        soma = v1 + v2
        print(soma)
    elif escolha == 2:
        multi = v1 * v2
        print(multi)
    elif escolha == 3:
        if v1 > v2:
            print('O primeiro valor {} é maior'.format(v1))
        elif v1 < v2:
            print("O segundo valor {} é maior".format(v2))
        else:
            print("Os dois números são iguais ")
    elif escolha == 4:
        v1 = int(input("Digite o novo primeiro valor: "))
        v2 = int(input("Digite o novo segundo valor: "))
        print("O novos valores escolhidos foram {} e {}".format(v1, v2))
    elif escolha == 5:
        certeza = str(input('Tem certeza que deseja sair do programa [S/N]?')).strip().upper()[0]
        if certeza == 'S':
            break
    else:
        print("Digite uma opção válida")'''

# resolução do guanabara
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior 
[ 4 ] novos números 
[ 5 ] sair do programa''')
    opção = int(input("Qual é a sua opção?: "))
    if opção == 1:
        soma = n1 + n2
        print(soma)
    elif opção == 2:
        multi = n1 * n2
        print(multi)
    elif opção == 3:
        if n1 > n2:
            print('O primeiro valor {} é maior'.format(n1))
        elif n1 < n2:
            print("O segundo valor {} é maior".format(n2))
        else:
            print("Os dois números são iguais ")
    elif opção == 4:
        n1 = int(input("Digite o novo primeiro valor: "))
        n2 = int(input("Digite o novo segundo valor: "))
        print("O novos valores escolhidos foram {} e {}".format(n1, n2))
    elif opção == 5:
        print("Finalizando...")
    else:
        print("Digite uma opção válida")
    print('=-=' * 10)
    sleep(2)
print("Fim do programa! Volte sempre!")

