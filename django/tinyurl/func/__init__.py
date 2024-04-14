import pyshorteners
import mysql.connector
from cabecalho import cabecalho
from time import sleep


def encurtador(url):
    conexao_banco, cursor = estabelecer_conexao()
    shortener= pyshorteners.Shortener()
    shorted_link=shortener.tinyurl.short(url)

    print(f"A sua url encurtada é : {shorted_link} ")
    try:  
        comando = ("""INSERT INTO urls (urlencur, urlnormal)
                   VALUES (%s, %s)""")
        dados = (shorted_link,url)
        cursor.execute(comando,dados)
        conexao_banco.commit()
    except mysql.connector.Error as e:
        print(f"ERRO {e}")
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
                print(f"Os seus urls encurtados são: ulrs: {url}")
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
        print(f"Os seus urls encurtados são: ulrs: {url}")
    
    except (mysql.connector.Error) as e:
        print(f"Error : {e}")
    finally:
        cursor.close()
        conexao_banco.close()



def estabelecer_conexao():
    try:
        conexao_banco = mysql.connector.connect(
            host="localhost",
            user= "root",
            password="",
            database="horastrabalhadas"
        )
        
    except (mysql.connector.Error) as e:
        print(f"Erro {e} // ao tentar estabelecer a conexão")

    cursor = conexao_banco.cursor()

    return conexao_banco,cursor


def fimprograma():
    print("fechando a aplicacão...")
    sleep(2.0)
    cabecalho("FIM DO PROGRAMA")
