# maior e menor valores em tuplas
from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10),
    randint(1, 10), randint(1, 10))
print(f'Eu sorteei o valor de {n}')
print(f'O menor número é {min(n)}')
print(f'O maior número é {max(n)}')

