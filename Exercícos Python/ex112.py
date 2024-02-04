# site está acessível?
import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://pudim.com.br")
except:
    print('Deu erro')
else:
    print('Tudo ok')
    print(site.read())
