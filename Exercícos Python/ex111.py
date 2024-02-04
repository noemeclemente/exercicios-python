def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número válido')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não usar esse número')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número real válido')
            continue
        except (KeyboardInterrupt):
            print('O usuário não quis digitar esse número')
            return 0
        else:
            return n

n1= leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f"O valor inteiro digitado foi {n1}, e o real foi {n2}")