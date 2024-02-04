# função para fatorial

def fatorial(n, show=False):
    """
    Calcula o fatorial de um número
    :param n: o número a ser calculado
    :param show: mostrar ou não a conta
    :return: fatorial de n 
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(f' X ', end=' ')
            else:
               print(' = ', end=' ')
        f *= c
    return f


print(fatorial(5, show=True))