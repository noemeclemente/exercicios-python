# contando vogais em tupla

palavras = ('Amanha', 'Saudade', 'Noite', 'Alvorada',
            'Crepusculo', 'Embriaguez', 'Solitude', 'Amor')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos', end =' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')