# reajuste salarial

'''
sal = float(input("Qual é o seu salário atual: "))
novo = sal * 15/100
atual = sal + novo

print("O seu salário atual é de {} reais, com o reajuste de 15% ele aumentará em {} reais, totalizando {}".format(sal, novo, atual))
'''

sal = float(input("Qual é o seu salário atual: "))
novo = sal + (sal * 15/100)
print("O seu salário atual é de {}".format(novo))