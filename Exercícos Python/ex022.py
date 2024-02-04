# procurando uma string dentro de outra

''' nome = str(input("Qual o seu nome completo: ")).strip()
print("Seu nome tem silva? {}".format( "silva" in nome.lower())) '''

nome = str(input("Qual o seu nome completo?")).strip()
print("Tem Camargo no seu nome? {}".format('camargo' in nome.lower()))