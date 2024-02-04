# analisando e gerando dicionários

def notas(*n, sit=False):
    """

    :param n: notas que vão ser inseridas, mais de uma *
    :param sit: mostrar a situação, iniciar cm false é o padrão
    :return: retornará o dicionário r, criado dentro da função
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'

    return r


resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)