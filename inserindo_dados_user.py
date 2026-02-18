import mysql.connector

from mysql.connector import Error


print('Rotina para cadastro de produtos no banco de dados\n')
print('Entre com os dados conforme solicitado')

IdProd = input('Id Produto: ')

NomeProd = input('Nome do Produto: ')

PrecoProd = input("Preço: ")

QtdeProd = input('Quantidade: ')


dados = IdProd + ',\'' + NomeProd + '\',' + PrecoProd + ',' + QtdeProd + ')'

declaracao ="""INSERT INTO kair_teste
(IdTeste, NomeTeste, PrecoTeste, QuantidadeTeste)
VALUES ("""

sql = declaracao + dados


try:
    conexao = mysql.connector.connect (
        host = 'localhost',

        database = 'kair_pizzaria',

        user = 'root',

        password = ''

    )

    inserir_produtos =  sql

    cursor = conexao.cursor()

    cursor.execute(inserir_produtos)

    conexao.commit()
    print(cursor.rowcount, "Registros inseridos na tabela!")
    cursor.close()

except Error as erro:
    print(f'Falha ao inserir os dados: {erro}')

finally:
    if (conexao.is_connected()):
        cursor.close()
        conexao.close()
        print("Conexão finalizada!")