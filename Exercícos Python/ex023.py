# primeira e última ocorrência
from unidecode import unidecode
frase = str(input("Digite uma frase: ")).upper().strip()
frase1 = unidecode(frase)
print("A letra A aparece {} vezes".format(frase1.count('A')))
print("A primeira letra A aparece na posição {}".format(frase1.find('A')+1))
print('A última letra A aparece na posição {}'.format(frase1.rfind('A')+1))