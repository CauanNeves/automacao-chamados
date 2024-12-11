from table_pc import prompt_cls, Table_pc
from table_printer import Table_Printer
from datetime import datetime
from time import sleep
from colorama import Fore



cumprimentos= 'Bom dia!' if datetime.now().hour < 12 else 'Boa tarde!'

def main_menu():
    prompt_cls()
    print(Fore.GREEN + f'{cumprimentos} digite o número da opção que deseja:\n 0. Manutenção de computadores e Monitor.\n 1. Solicitação de toner.\n 2. Sair.')
    to_do= input(Fore.CYAN + 'Opção desejada:')
    return to_do

def main():
    while True:
        to_do= main_menu()
        while to_do not in ['0', '1', '2']:
            print(Fore.RED + 'A opção informada não consta no programa.')
            sleep(1)
            to_do= main_menu()

        if to_do == '0':
            Table_pc.main()
        
        elif to_do == '1':
            Table_Printer.main()
        
        elif to_do == '2':
            break
    

if __name__ == '__main__':
    main()