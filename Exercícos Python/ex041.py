# gerenciador de pagamentos

print(f'{"LOJAS GUANABARA":=^40}')
preco = float(input("Qual é o preço dos produtos: "))
print(''' FORMAS DE PAGAMENTO
 [1] à vista dinheiro/cheque 
 [2] a vista no cartão 
 [3] em até 2x no cartão
 [4] 3x ou mais no cartão ''')
opcao = int(input("Qual é a sua opção? : "))

if opcao == 1:
    total = preco - (preco*10)/100
elif opcao == 2:
    total = preco - (preco*5)/100
elif opcao == 3:
    total = preco
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R${:.2f}".format(parcela))
elif opcao == 4:
    total = preco + (preco*20)/100
    totparc = int(input("Em quantas parcelas?: "))
    parcela = preco / totparc
    print("Sua compra será parcelada em {}x de {:.2f} com juros".format(totparc, parcela))
else:
    print("Digite uma opção valida")
print("Você pagará no total o valor de {:.2f}".format(total))