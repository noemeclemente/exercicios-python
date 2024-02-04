# funções para votar
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 and idade < 65:
        return f'O voto com {idade} é obrigatório'
    else:
        return f'Votar com {idade} anos é obrigatório'



anonasc = int(input('Ano de nascimento:'))
print(voto(anonasc))