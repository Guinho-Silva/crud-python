import mysql.connector

try:

#Cria a conexão com o banco
    conexao = mysql.connector.connect(

        host = 'localhost',

        database = 'kair_pizzaria',

        user = 'root',

        password = ''
    )

    cria_tabela = """CREATE TABLE kair_teste(
    IdTeste int(11) NOT NULL,
    NomeTeste VARCHAR(70) NOT NULL,
    PrecoTeste DECIMAL(10,2) NOT NULL,
    QuantidadeTeste TINYINT NOT NULL,
    PRIMARY KEY (IdTeste)

    )"""

    cursor = conexao.cursor()

    cursor.execute(cria_tabela)

    print("Tabela criada com sucesso!")

except mysql.connector.Error as erro:
    print("Falha ao criar a tabela: {}".format(erro))

finally:
    if (conexao.is_connected()):
        cursor.close()
        conexao.close()
        print("Conexão encerrada!")