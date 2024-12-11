import os
from colorama import Fore, Style
from tabulate import tabulate
from datetime import datetime

def exibir_dados(self, dados):
    # Cria uma tabela com os dados
    tabela = [["Campo", "Valor"]]  # Cabeçalho da tabela
    for chave, valor in dados.items():
        tabela.append([chave.capitalize(), valor])  # Adiciona os dados à tabela
    
    print(tabulate(tabela, headers='firstrow', tablefmt='fancy_grid'))


def navbar():
    '''Exibe a barra de navegação no terminal.'''
    print(f"{Fore.CYAN + Style.BRIGHT + '=' * 40}\n{Fore.GREEN + Style.BRIGHT + 'Solicitação de reparo'.center(40)}\n{Fore.CYAN + Style.BRIGHT + '=' * 40}")

def prompt_cls():
    #limpa o terminal
    os.system('cls' if os.name== 'nt' else 'clear')

def pausar():
    '''Pausa a execução e aguarda o usuário pressionar Enter.'''
    input(Fore.YELLOW + 'Pressione Enter para continuar...')

class Solicitacao:

    def exibir_dados(self, dados):
        # Cria uma tabela com os dados
        tabela = [["Campo", "Valor"]]  # Cabeçalho da tabela
        for chave, valor in dados.items():
            tabela.append([chave.capitalize(), valor])  # Adiciona os dados à tabela
    
        print(tabulate(tabela, headers='firstrow', tablefmt='fancy_grid'))

    def main(self):
        self.all_data= []
        while True:
            prompt_cls()
            navbar()
            print(Fore.GREEN + 'Bom dia! Informe o que for solicitado abaixo.\n' if datetime.now().hour < 12 else Fore.GREEN + 'Boa tarde! Informe o que for solicitado abaixo.\n')

            #Patrimonio
            self.patrimonio_value= None
            while self.patrimonio_value == None:
                try:
                    self.patrimonio_value= int(input(Fore.BLUE + 'Número de patrimônio:\n'))
                except:
                    print(Fore.RED + 'O número de patrimônio não pode conter letras, espaços ou símbolos. Apenas números\n')
                    
                    
            #Número de Host
            have_host= input(Fore.GREEN + 'Possui Número de etiqueta PMAR/SAD.SSI? (s/n)').upper()
            while have_host not in ['S', 'N']:
                print(Fore.RED + 'Por favor, responda com "s" para sim ou "n" para não.')
                have_host= input('Possui Número de etiqueta PMAR/SAD.SSI? (s/n)').upper()
                
            self.host_value = ''
            if have_host == 'S':   
                while self.host_value == '':
                    try:
                        self.host_value= int(input(Fore.LIGHTYELLOW_EX + 'Número da etiqueta PMAR/SAD.SSI:\n'))
                    except:
                        print(Fore.RED + 'O número da etiqueta PMAR não pode conter letras, espaços ou símbolos. Apenas números\n')
                        self.host_value = ''
            
            
            #Marca
            self.marca_value = ''
            while self.marca_value == '':
                self.marca_value= input(Fore.BLUE + 'Marca:\n')
                

            #Local
            self.local_value = ''
            while self.local_value == '':
                self.local_value= input(Fore.LIGHTYELLOW_EX + 'Local/ unidade:\n')
                
                
            #Descrição
            self.descricao_value = ''
            while self.descricao_value == '':
                self.descricao_value= input(Fore.BLUE + 'Descrição do problema:\n')
            
            self.data = {
            'patrimonio': self.patrimonio_value,
            'host': self.host_value,
            'marca': self.marca_value,
            'descrição': self.descricao_value,
            'local': self.local_value
            }

            self.exibir_dados(self.data)

            #Verifica se o usuário deseja corrigir alguma informação
            corrigir = input(Fore.GREEN + 'Deseja corrigir algo? (s/n) ').upper()
            while corrigir not in ['S', 'N']:
                print(Fore.RED + 'Por favor, responda com "s" para sim ou "n" para não.')
                corrigir = input(Fore.GREEN + 'Deseja corrigir algo? (s/n) ').upper()
            if corrigir == 'S':
                pass
            else:
                self.all_data.append(self.data)
                add= input(Fore.GREEN + 'Deseja adicionar mais itens? (s/n)').upper()
                while add not in ['S', 'N']:
                    print(Fore.RED + 'Por favor, responda com "s" para sim ou "n" para não.')
                    add= input(Fore.GREEN + 'Deseja adicionar mais itens? (s/n)').upper()
                if add != 'S':
                    break
                
        # Exibir todas as solicitações
        print(Fore.GREEN + "Todas as solicitações:")
        for id, solicitacao in enumerate(self.all_data, start=1):
            print(Fore.CYAN + f"Solicitação {id}:")
            self.exibir_dados(solicitacao)
                
if __name__ == '__main__':
    solicitacao= Solicitacao()
    solicitacao.main()