# analisando triângulos v2

s1 = float(input("Primeiro segmento: "))
s2 = float(input("Segundo segmento: "))
s3 = float(input("Terceiro segmento: "))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2: # um lado não pode ser maior do que asoma dos outros dois
    print("Forma um triângulo")
    if s1 == s2 == s3:
        print("Esse triângulo é equilátero pois todos os lados são iguais")
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print("Esse triângulo é isóceles pois há dois lados iguais")
    elif s1 != s2 and s1 != s3 and s2 != s3:
        print("Esse triângulo é escaleno pois todos os lados são diferentes")
else:
    print("Não forma um triângulo")