import pyshorteners
import mysql.connector
from cabecalho import cabecalho
from time import sleep
from banco_dados import estabelecer_conexao


def encurtador(url):
    conexao_banco, cursor = estabelecer_conexao()
    shortener= pyshorteners.Shortener()
    shorted_link=shortener.tinyurl.short(url)

    print(f"\033[34mA sua url encurtada é : {shorted_link}\033[m ")
    try:  
        comando = ("""INSERT INTO urls (urlencur, urlnormal)
                   VALUES (%s, %s)""")
        dados = (shorted_link,url)
        cursor.execute(comando,dados)
        conexao_banco.commit()
    except mysql.connector.Error as e:
        print(f"\033[31mERRO {e}\033[m")
    finally:
        conexao_banco.close()
        cursor.close()


def createtable():
    conexao_banco, cursor = estabelecer_conexao()
    try:
        comando = ("""CREATE TABLE urls (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    urlencur VARCHAR(255) NOT NULL,
                    urlnormal VARCHAR(255)
                    )""")
        cursor.execute(comando)
        conexao_banco.commit()
    except mysql.connector.Error as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()
        conexao_banco.close()
        print("Tabela criada com sucesso!")

        
def viewurls():
    try:
        conexao_banco, cursor = estabelecer_conexao()
        comando = ("SELECT urlencur from urls")
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
                url = i
                print(f"\033[34mOs seus urls encurtados são: ulrs: {url}\033[m")
    except (mysql.connector.Error) as e:
        print(f"Error : {e}")
    finally:
        cursor.close()
        conexao_banco.close()
    
    
def viewurlnrm():
    try:
        conexao_banco,cursor = estabelecer_conexao()

        comando = ("SELECT urlnormal FROM urls")
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            url = i
        print(f"\033[34mOs seus urls encurtados são: ulrs: {url}\033[m")
    
    except (mysql.connector.Error) as e:
        print(f"Error : {e}")
    finally:
        cursor.close()
        conexao_banco.close()


def fimprograma():
    print("\033[31mfechando a aplicacão...\033[m")
    sleep(2.0)
    cabecalho("\033[35mFIM DO PROGRAMA\033[m")
