# cosseno e tangente
from math import radians, sin, cos, tan
angulo = float(input("Digite o número que você deseja: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("O ângulo de {} tem o seno de {:.2f} \nO cosseno é {:.2f} \nA tangente é {:.2f}".format(angulo, seno, cosseno, tangente))