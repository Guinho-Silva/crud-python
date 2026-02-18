import mysql.connector

from mysql.connector import Error


#Atualizar registros de um banco de dados

def conectar():
    try:
        global conexao

        conexao = mysql.connector.connect(
            host = 'localhost',
            database = 'kair_pizzaria',
            user = 'root',
            password = ''
        )
    except:
        print('Erro de conexão!')

def consulta(idProd):
    try:
        conectar()
        consulta_sql = "SELECT * FROM kair_teste WHERE IdTeste = %s"
        cursor = conexao.cursor()
        cursor.execute(consulta_sql, (idProd,))
        linhas = cursor.fetchall()

        for valor in linhas:
            print('ID:', valor[0])
            print('Produto:', valor[1])
            print('Preço:', valor[2])

    except Error as erro:
        print(f'Falha ao consultar a tabela: {erro}')
    
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


def atualiza(declacao):
    try:
        conectar()

        altera_preco = declacao

        cursor = conexao.cursor()

        cursor.execute(altera_preco)

        conexao.commit()

        print('Preço alterado com sucesso')

    except Error as erro:
        print(f'Falha ao inserir dados na tabela: {erro}')

    finally:
        if(conexao.is_connected()):
            cursor.close()
            conexao.close()

# Corpo principal

if __name__=='__main__':

    print('Atualizar preços de produtos no banco de dados')
    
    print('Entre com os dados conforme solicitado: ')

    print('\nDigite o código do produto a alterar:')

    idprod = input('Id do Produto: ')

    consulta(idprod)

    print('\nEntre com o novo preço do produto: ')

    precoProd = input('Novo Preço: ')


    declaracao = """UPDATE kair_teste SET PrecoTeste = """ + precoProd + """ WHERE IdTeste = """ + idprod

    #Executa o UPDATE da declaração
    atualiza(declaracao)

    verifica = input("\nDeseja consultar a atualização? [S/N]").upper()

    if verifica == 'S':
        consulta(idprod)
    else:
        print('\nAté mais')