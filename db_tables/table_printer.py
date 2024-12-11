import sqlite3
import os
from colorama import Fore, Style
from tabulate import tabulate

#Indo até o diretório do Banco de Dados
os.chdir('C:\\database')

#Conectando
connection= sqlite3.connect('chamado_info.db')
cursor= connection.cursor()

#Exibir a tabela Solicitacao_Toner do banco de dados
def show_datas():
    cursor= connection.cursor()
    cursor.execute('SELECT * FROM Solicitacao_Toner')
    datas= cursor.fetchall()
    cursor.close()
    
    table= [['Id', 'Marca', 'Modelo', 'Quantidade', 'Data de Solicitação']]
    for row in datas:
        table.append(list(row))
    
    print(tabulate(table, headers= 'firstrow', tablefmt= 'fancy_grid'))
    
#---------------Funções do Prompt--------------------
def navbar():
    '''Exibe a barra de navegação no terminal.'''
    print(f"{Fore.CYAN + Style.BRIGHT + '=' * 70}\n{Fore.GREEN + Style.BRIGHT + 'Solicitações de Toner'.center(70)}\n{Fore.CYAN + Style.BRIGHT + '=' * 70}")
    
def prompt_cls():
    #limpa o terminal
    os.system('cls' if os.name== 'nt' else 'clear')

class Table_Printer:
    def main():
        prompt_cls()
        navbar()
        show_datas()
        input('Pressione enter para sair...')
        cursor.close()

if __name__ == '__main__':
    table= Table_Printer()
    table.main()