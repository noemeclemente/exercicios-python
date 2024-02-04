# grupo da maioridade
from datetime import datetime
c1 = 0
c2 = 0
for a  in range(1, 7 ):
    ano = int(input("Em que ano a {}ª pessoa nasceu: ".format(a)))
    idade = datetime.now().year - ano
    if idade >= 18:
        c1 += 1
    else:
        c2 += 1
print("Há {} pessoas maiores de idade e {} pessoas menores de idade".format(c1, c2))