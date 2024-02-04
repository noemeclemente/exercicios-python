# validando expressões numéricas

ex = str(input('Digite uma expressão: '))
pilha = []
for simb in ex:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão não é válida')