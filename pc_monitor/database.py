import sqlite3
import os
from datetime import datetime

#Verificando se o diretório existe e criando apenas se necessário
os.makedirs('C:\\database', exist_ok= True)

class DataBase:
    def __init__(self, db_path):
        # Definindo o caminho para o banco de dados
        self.db_path = db_path

    def add(self, local, patrimonio, host):
        # Conectando-se ao Banco de Dados
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Criando a tabela
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Pc_Monitor(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    local TEXT NOT NULL,
                    patrimonio INTEGER NOT NULL,
                    host INTEGER,
                    data_abertura TEXT NOT NULL,
                    data_ida TEXT,
                    data_volta TEXT,
                    data_entrega TEXT
                );
            ''')

            # Adicionando dados
            date = datetime.now().strftime('%Y-%m-%d')
            cursor.execute('INSERT INTO Pc_Monitor (local, patrimonio, host, data_abertura) VALUES (?, ?, ?, ?)', (local, patrimonio, host, date))

            # As alterações são automaticamente confirmadas quando usamos "with"

