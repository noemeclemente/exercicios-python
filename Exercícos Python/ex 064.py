
while True:
    n = int(input('Digite um valor para ver sua tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        resp = c * n
        print(f'{n} X {c} = {resp}')

