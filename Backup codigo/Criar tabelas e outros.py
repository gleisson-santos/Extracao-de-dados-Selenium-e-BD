import pyodbc

def executar_conexao():
        server   = 'DESKTOP-0P0H9IO'
        database = 'ControlePav'
        #username = 'gleisson.santos'
        #password = '1234'
        conexao = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)
        #conexao = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)#+';UID='+username+';PWD='+ password
        print('Conexão com o BD Bem Sucessido!')

        cursor = conexao.cursor()
        criar_tabela = """ 
            CREATE TABLE Dados (
                tipo_pavimento  VARCHAR(50),
                id_equipe       VARCHAR (50),
                datas           DATE,
                metragem_1x     DECIMAL(8,2),
                metragem_2x     DECIMAL(8,2),
                observacoes     VARCHAR (50),
                ss              VARCHAR(500)
        ); 
        """

        cursor.execute(criar_tabela)
        cursor.commit()
