from func import escurtador
from cabecalho import cabecalho,opcoes
from banco_dados import db
from time import sleep


sleep(1.5)
db()
sleep(1.0)
cabecalho("ENCURTADOR DE URLS")

opcoes()
res = int(input("Sua opcão:"))



if res == 1:
    url=input("Enter the Link:")
    escurtador(url)
#elif res == 2:
    
    
        

