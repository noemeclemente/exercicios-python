# detector de palíndromo
# palavra igual de trás pra frente

# forma do guanabara fazer
'''
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra] # adiciona cada caractere ao final da string inverso
if junto == inverso:
    print("Essa frase é um palíndromo")
else:
    print("Essa frase não é um palíndromo") '''

# forma alternativa

frase = str(input("Digite uma frase: ")).upper().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("Essa frase não é um palíndromo")