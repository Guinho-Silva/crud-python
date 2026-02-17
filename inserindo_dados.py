import mysql.connector

from mysql.connector import Error
'''try:
    conexao = mysql.connector.connect(

        host = 'localhost',

        database = 'kair_pizzaria',

        user = 'root',

        password = ''

    )

    insere_sql = """
        INSERT INTO kair_teste
            (IdTeste, NomeTeste, PrecoTeste, QuantidadeTeste)

        VALUES
            (1, 'Câmera', 850.00,5),
            (2, 'Monitor', 630.00,7),
            (3, 'Relógio', 575.00,10)
    
    
    """

    cursor = conexao.cursor()

    cursor.execute(insere_sql)

    conexao.commit() # Quando usamos querys de manipulação de dados, devemos usar o commit, pois ele finaliza a transação (grava)
    print(cursor.rowcount, "Registros inseridos com sucesso!")

    cursor.close()

except Error as erro:
    print(f'Falha ao inserir os dados: {erro}')


finally:
    if (conexao.is_connected()):
        cursor.close()
        conexao.close()
        print("Conexão finalizada!")'''


#Script para verificar os dados


try:

    conexao = mysql.connector.connect(

        host = 'localhost',

        database = 'kair_pizzaria',

        user = 'root',

        password = ''

    )


    consulta = "SELECT * FROM kair_teste"

    cursor = conexao.cursor()

    cursor.execute(consulta)

    linhas = cursor.fetchall()

    print("Número total de registros", cursor.rowcount)

    print("\nMotrar os produtos cadastrados\n")

    for valor in linhas:
        print("Id_Produto:", valor[0])
        print('Nome do Produto:', valor[1])
        print('Preço:', valor[2])
        print('Quantidade:', valor[3], "\n")

except Error as erro:
    print('erro ao acessar tabela', erro)

finally:
    if (conexao.is_connected()):
        cursor.close()
        conexao.close()
        print("Conexão encerrada!")