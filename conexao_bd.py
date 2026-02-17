import mysql.connector

#Cria conexão ao banco de dados
conexao = mysql.connector.connect(
    host = 'localhost',

    database = 'kair_pizzaria',

    user = 'root',

    password = ''
)

#Verifica se está conectado ao banco e seleciona ele
if conexao.is_connected():
    db_info = conexao.server_info
    print("Conectado ao servidor", db_info)

    cursor = conexao.cursor()

    cursor.execute("SELECT DATABASE();")

    linha =  cursor.fetchone()
    print("Conectado ao banco de dados", linha)
#Encerra a conexão ao banco, deletando a memória
if conexao.is_connected():
    cursor.close()
    conexao.close()
    print("Conexão ao MySQl encerrada!")