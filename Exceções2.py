# crie um codigo em python que testa se o computador consegue acessar um site

import urllib.request
from time import sleep

try:
    print("Estabelecendo uma conexão, por favor aguarde.")
    sleep(3)
    urllib.request.urlopen('https://www.youtube.com/')
except:
    print(f"Não foi possível acessar o site.")
else:
    print("O site está funcionando corretamente.")




