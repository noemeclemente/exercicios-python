# maior e menor valores

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
     n = int(input('Digite um número: '))
     soma += n
     quant += 1
     if quant == 1:
        maior = menor = n
     else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n

     resp = str(input('Deseja continuar: [S/N]?')).upper().strip()[0]
média = soma / quant
print('Acabou')
print('A média entre todos os {} números digitados é {}, o maior é {} e o menor é {}'.format(quant, média, maior, menor))