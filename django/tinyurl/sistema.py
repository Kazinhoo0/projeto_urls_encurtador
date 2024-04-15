from func import encurtador,viewurls,viewurlnrm,createtable,fimprograma
from cabecalho import cabecalho,opcoes
from banco_dados import estabelecer_conexao
from time import sleep


sleep(1.5)
estabelecer_conexao()
sleep(1.0)
cabecalho("\033[33mENCURTADOR DE URLS\033[m")

opcoes()
while True:
    try:
        res = int(input("\033[34mSua opcão:\033[m"))
        break
    except (TypeError,ValueError):
        print("\033[31mERRO!!, Insira apenas números inteiros porfavor...\033[m")


while True:
    if res == 1:
        url=input("\033[33mEnter the Link:\033[m")
        encurtador(url)
    elif res == 2:
        viewurls()
    if res == 3:
        viewurlnrm()
    if res == 4:
        fimprograma()
        break
    if res == 5:
        createtable()