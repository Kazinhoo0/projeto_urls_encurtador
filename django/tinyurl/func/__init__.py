import pyshorteners
from banco_dados import db
import mysql.connector

def encurtador(url):

    shortener=pyshorteners.Shortener()

    shorted_link=shortener.tinyurl.short(url)

    print(f"A sua url encurtada é : {shorted_link} ")


def createtable():
    conexao_banco,cursor = estabelecer_conexao()
    try:
        comando = ("""CREATE TABLE urls (
                id auto_increment, not_null
                urlencur varchar(50)
                urlnormal varchar(200) 
                   """)
        cursor.execute(comando)
        cursor.fetchall()
    except (TypeError) as e:
        print(f"Erro: {e}")
    except (mysql.connector.Error) as e:
        print(f"Error : {e}")
    finally:
        cursor.close()
        conexao_banco.close()
        return print("Tabela criada com Sucesso!")
        


def viewurls(comando):
    try:
        conexao_banco,cursor = estabelecer_conexao
        createtable()

        comando = ("SELECT * FROM urlencur")
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
                url = i
                print(f"Os seus urls encurtados são: 
                ulrs: {url}")
    except (mysql.connector.Error) as e:
        print(f"Error : {e}")
    finally:
        cursor.close()
        conexao_banco.close()
    


def viewurlnrm(comando):
    try:
        conexao_banco,cursor = estabelecer_conexao
        createtable()

        comando = ("SELECT * FROM urlnormal")
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
                url = i
                print(f"Os seus urls encurtados são: 
                ulrs: {url}")
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