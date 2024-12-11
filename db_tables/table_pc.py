import sqlite3
import os
from colorama import Fore, Style, init
from tabulate import tabulate
from datetime import datetime
from time import sleep


#------------------------Funções SQL------------------------------------

# Indo até o diretório do banco de dados
os.chdir('C:\\database')

# Conectando ao banco de dados
connection = sqlite3.connect('chamado_info.db')
cursor = connection.cursor()

# Exibe todas as linhas
def show_datas():
    cursor = connection.cursor()  # Cria um cursor local
    cursor.execute('SELECT * FROM Pc_Monitor')
    datas = cursor.fetchall()
    cursor.close() #Fecha o cursor
    
    table = [['Id', 'Local', 'Patrimônio', 'Host', 'Data de Abertura', 'Data de Ida', 'Data de Devolução', 'Data de Entrega']]
    for row in datas:
        table.append(list(row))
        
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

# Exibir as linhas que estão faltando a data de ida, volta ou entrega   
def dates_null(value):
    cursor = connection.cursor()  # Cria um cursor local
    if value == 'ida':
        cursor.execute('SELECT * FROM Pc_Monitor WHERE data_ida IS NULL')
    elif value == 'volta':
        cursor.execute('SELECT * FROM Pc_Monitor WHERE data_volta IS NULL')
    elif value == 'entrega':
        cursor.execute('SELECT * FROM Pc_Monitor WHERE data_entrega IS NULL')
        
    datas = cursor.fetchall()
    cursor.close() #Fecha o cursor
    
    table = [['Id', 'Local', 'Patrimônio', 'Host', 'Data de Abertura', 'Data de Ida', 'Data de Devolução', 'Data de Entrega']]
    for row in datas:
        table.append(list(row))
    
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

#Validando se o Id existe na tabela
def validate_id(id):
    cursor.execute('SELECT EXISTS(SELECT 1 FROM Pc_Monitor WHERE id=?)', (id,))
    return cursor.fetchone()[0]

#Validando se o Id existe na tabela que está faltando as datas de ida, volta ou entrega
def validate_update(id, value):
    if value == 'ida':
        cursor.execute('SELECT EXISTS(SELECT 1 FROM Pc_Monitor WHERE id=? AND data_ida IS NULL)', (id,))
    elif value == 'volta':
        cursor.execute('SELECT EXISTS(SELECT 1 FROM Pc_Monitor WHERE id=? AND data_volta IS NULL)', (id,))
    elif value == 'entrega':
        cursor.execute('SELECT EXISTS(SELECT 1 FROM Pc_Monitor WHERE id=? AND data_entrega IS NULL)', (id,))

    return cursor.fetchone()[0]

#Adicionando a datas
def update_data(ids, value):
    if value == 'ida':
        for id in ids.split():
            if validate_update(id, 'ida') == 0:
                print(Fore.RED + '\nId selecionado não é válido.')
                sleep(1)
                return
            date = datetime.now().strftime('%Y-%m-%d')
            cursor.execute('UPDATE Pc_Monitor SET data_ida = ? WHERE id = ?', (date, id))
    elif value == 'volta':
        for id in ids.split():
            if validate_update(id, 'volta') == 0:
                print(Fore.RED + '\nId selecionado não é válido.')
                sleep(1)
                return
            date = datetime.now().strftime('%Y-%m-%d')
            cursor.execute('UPDATE Pc_Monitor SET data_volta = ? WHERE id = ?', (date, id))
    
    elif value == 'entrega':
            for id in ids.split():
                if validate_update(id, 'entrega') == 0:
                    print(Fore.RED + '\nId selecionado não é válido.')
                    sleep(1)
                    return
                date = datetime.now().strftime('%Y-%m-%d')
                cursor.execute('UPDATE Pc_Monitor SET data_entrega = ? WHERE id = ?', (date, id))   
        
    show_datas()
    
    confirm= input(Fore.GREEN + 'Salvar? (s/n)').upper()
    while confirm not in ['S', 'N']:
        print(Fore.RED + 'Por favor, responda com "s" para sim ou "n" para não.')
        confirm= input(Fore.GREEN + 'Salvar? (s/n)').upper()
    
    if confirm == 'S':
        connection.commit()
        print(Fore.GREEN + 'Alterações salvas com sucesso.')
        sleep(1)
    else:
        connection.rollback()
        print(Fore.GREEN + 'Alterações Descartadas')

# Excluir alguma linha
def del_row(id):
    if validate_id(id) == 0:
        print(Fore.RED + '\nId selecionado não é válido.')
        sleep(1)
        return
    
    cursor.execute('DELETE FROM Pc_Monitor WHERE id = ?', (id,))
    
    # Mostra a tabela após a exclusão (não confirmada ainda)
    show_datas()
    
    # Pergunta ao usuário se deseja salvar a alteração
    confirm = input('Salvar? (s/n) ').upper()
    while confirm not in ['S', 'N']:
        print(Fore.RED + 'Por favor, responda com "s" para sim ou "n" para não.')
        confirm = input('Salvar? (s/n) ').upper()
            
    # Se a resposta for 'S', faz o commit
    if confirm == 'S':
        connection.commit()  # Salva as alterações no banco de dados
        print(Fore.GREEN + 'Alterações salvas com sucesso.')
        sleep(1)
    else:
        connection.rollback()  # Desfaz as alterações não salvas
        print(Fore.GREEN + 'Alterações descartadas.')
        sleep(1)

#---------------Funções do Prompt--------------------
def navbar():
    '''Exibe a barra de navegação no terminal.'''
    print(f"{Fore.CYAN + Style.BRIGHT + '=' * 110}\n{Fore.GREEN + Style.BRIGHT + 'Tabela Informática'.center(110)}\n{Fore.CYAN + Style.BRIGHT + '=' * 110}")
    
def prompt_cls():
    #limpa o terminal
    os.system('cls' if os.name== 'nt' else 'clear')

#Menu principal
def main_menu():
    prompt_cls()
    navbar()
    show_datas()
    
    print(Fore.GREEN + 'Opções:\n  0. Adicionar data de ida a informática\n  1. Adicionar data de volta da manutenção\n  2. Adicionar data de entrega\n  3. Excluir linha\n  4. Sair')
    to_do= input(Fore.CYAN + 'Informe o que deseja:')
    return to_do

class Table_pc:
    def main():
        try:
            while True:
                to_do = main_menu()            
                while to_do not in ['0', '1', '2', '3', '4']:
                    print(Fore.RED + 'A opção informada não consta no programa.')
                    sleep(1)
                    to_do = main_menu()

                if to_do == '0':
                    prompt_cls()
                    navbar()
                    dates_null('ida')
                    id = input(Fore.CYAN + 'Informe o id da linha que deseja adicionar a data de ida:')
                    if id != '':
                        update_data(id, 'ida')
                    else:
                        pass

                elif to_do == '1':
                    prompt_cls()
                    navbar()
                    dates_null('volta')
                    id = input(Fore.BLUE + 'Informe o id da linha que deseja adicionar a data de volta:')
                    if id != '':
                        update_data(id, 'volta')
                    else:
                        pass
                
                elif to_do == '2':
                    prompt_cls()
                    navbar()
                    dates_null('entrega')
                    id= input(Fore.BLUE + 'Informe o id da linha que deseja adicionar a data de volta:')
                    if id != '':
                        update_data(id, 'entrega')
                    else:
                        pass
                
                elif to_do == '3':
                    prompt_cls()
                    navbar()
                    show_datas()
                    id = input(Fore.BLUE + 'Informe o id da linha que deseja excluir:')
                    if id != '':
                        del_row(id)
                    else:
                        pass

                else:
                    break
        finally:
            connection.close()

if __name__ == '__main__':
    Table_pc.main()
