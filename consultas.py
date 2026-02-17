import mysql.connector


try:

    conexao = mysql.connector.connect(

        host = 'localhost',

        database = 'kair_pizzaria',

        user = 'root',

        password = ''


    )

    consulta = "SELECT * FROM cliente"

    cursor = conexao.cursor() #O objeto  cursor faz a iteração linha a linha dos registros de uma determinada tabela

    cursor.execute(consulta) #Executa a consulta criada

    linhas = cursor.fetchall() #Retornará todoas as linhas da tabela

    print("Número total de registro: ", cursor.rowcount) #Retorna todos os dados solicitados

    print("\nMostrando os nomes cadastrados")

    for valor in linhas:
        print("Id_cliente:", valor[0])
        print("Nome:", valor[4])
        print("Data_Nasc:", valor[2])
except mysql.connector.Error as erro:
    print("Erro ao acessar a tabela", erro)

finally:
    if (conexao.is_connected()):
        conexao.close()
        cursor.close()
        print("Conexão encerrada!")