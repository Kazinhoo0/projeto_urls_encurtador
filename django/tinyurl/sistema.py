from func import encurtador,viewurls,viewurlnrm,createtable,fimprograma
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
    encurtador(url)
elif res == 2:
    viewurls()
if res == 3:
    viewurlnrm()
if res == 4:
    fimprograma()
if res == 5:
    createtable()

    

    
    
        

