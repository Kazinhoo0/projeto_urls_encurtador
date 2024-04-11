import mysql.connector

def db():
    
    conexao_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="urlsencurtadas"
    )
    while True:
        try:
            print("Banco de dados conectado com sucesso!!")
            break
        except TypeError as e:
            print(f"ERRO! {e}")
            
            
    return conexao_db



