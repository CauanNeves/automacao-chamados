import sqlite3
import os
from datetime import datetime

#Verificando se o diretório existe e criando apenas se necessário
os.makedirs('C:\\database', exist_ok= True)

class DataBase:
    def __init__(self, db_path):
        self.db_path= db_path
    
    def add(self, marca, modelo, quantidade):
        #Conectando ao Banco de dados
        with sqlite3.connect(self.db_path) as conn:
            cursor= conn.cursor()
            
            #Criando a tabela
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Solicitacao_Toner(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    marca TEXT NOT NULL,
                    modelo TEXT NOT NULL,
                    quantidade INTEGER NOT NULL,
                    data_solicitacao TEXT NOT NULL
                );
            ''')

            #Adicionando dados
            date = datetime.now().strftime('%Y-%m-%d')
            cursor.execute('INSERT INTO Solicitacao_toner (marca, modelo, quantidade, data_solicitacao) VALUES (?, ?, ?, ?)', (marca, modelo, quantidade, date))

            # As alterações são automaticamente confirmadas quando usamos "with"

