'''
n = int(input("Digite um número: "))
d = n * 2
t = n * 3
r = n ** (1/2) # raiz quadrada
print("O dobro de {} vale {}.".format(n, d))
print("O triplo de {} vale {}. \nA raiz quadrada de {} vale {:.2f}".format(n, t, n, r))
'''

n = int(input("Digite um número: "))
print("O dobro de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} vale {:.2f}".format(n, (n*2), n, (n*3), n, (n **(1/2))))