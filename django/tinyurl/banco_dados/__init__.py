import mysql.connector

def estabelecer_conexao():
    try:
        conexao_banco = mysql.connector.connect(
            host="localhost",
            user= "root",
            password="",
            database="horastrabalhadas"
        )
        
    except (mysql.connector.Error) as e:
        print(f"\033[31mErro {e} // ao tentar estabelecer a conexão\033[m")

    cursor = conexao_banco.cursor()
    print("\033[32mConexão estabelecida com sucesso!!\033[m")

    return conexao_banco,cursor




