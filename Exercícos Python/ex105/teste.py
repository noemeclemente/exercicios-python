import moeda

p = float(input('Digite o preço: '))
print(f'A metade de R$ {p} e {moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p,10)}')
