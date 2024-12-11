import os
from colorama import Fore, Style, init
from tabulate import tabulate
from datetime import datetime

# Funções auxiliares fora da classe (pois não dependem do estado)
def navbar():
    '''Exibe a barra de navegação no terminal.'''
    print(f"{Fore.CYAN + Style.BRIGHT + '=' * 40}\n{Fore.GREEN + Style.BRIGHT + 'Solicitação de Toner'.center(40)}\n{Fore.CYAN + Style.BRIGHT + '=' * 40}")

def prompt_cls():
    '''Limpa a tela do terminal.'''
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    '''Pausa a execução e aguarda o usuário pressionar Enter.'''
    input(Fore.YELLOW + 'Pressione qualquer tecla para continuar...')

def exibir_menu(opcoes):
    '''Exibe o menu com formatação aprimorada.'''
    prompt_cls()
    navbar()
    print(tabulate(opcoes, headers=['Opção', 'Descrição'], tablefmt='fancy_grid'))

def obter_escolha(opcoes):
    '''Obtém a escolha do usuário e valida a entrada.'''
    while True:
        try:
            escolha = int(input(Fore.CYAN + 'Digite o número da opção desejada: '))
            if 0 <= escolha < len(opcoes):
                return escolha
            else:
                print(Fore.RED + 'Opção inválida. Por favor, escolha uma opção válida.')
        except ValueError:
            print(Fore.RED + 'Entrada inválida. Por favor, digite um número.')

# Classe que encapsula o estado e a lógica principal
class SolicitacaoToner:
    def __init__(self):
        self.escolhas = []  # Variável para armazenar as escolhas

        # Dicionário contendo os números de série correspondentes a cada modelo
        self.numeros_serie = {
            'OKI MB491': ['AK36058398A0', 'AK49010532A0', 'AK36058284A0', 'AK37041045A0', 'AK49010553A0', 'AK37008004A0', 'AK35062250A0', 'AK4A078872A0', 'AK36058213A0', 'AK22018954A0', 'AK37040285A0', 'AK36021103A0', 'AK4A023046A0', 'AK38017600A0', 'BRBSRCW0BJ', 'AK49010536A0', 'AK4A048875A0', 'AK36058235A0', 'AK49010554A0', 'AK48059982A0', 'AK4A068269A0', 'AK37007309A0', 'AK49010500', 'AK36057664A0', 'AK37007199A0', 'AK4A036111A0', 'AK36058195A0', 'AK37072654A0', 'AK4A035999A0', 'AK4A036109A0', 'AK48059129A0', 'AK4A048861A0', 'AK35062254A0', 'AK4A036101', 'AK37007310A0', 'AK49010559A0', 'AK37072677A0', 'AK37008115A0', 'AK36057660A0', 'AK35062230A0', 'AK37007293A0', 'AK4A048836A0', 'AK37007269A0', 'AK3506223BA0', 'AK35062274A0', 'AK48058256A0', 'AK49010547A0', 'AK37007205A0', 'AK37007229A0', 'AK38018061A0', 'AK37072611A0', 'AK4A048842A0', 'AK4A036006A0', 'AK4A036005A0', 'AK36058335A0', 'AK37008004A0', 'AK37072612A0', 'AK37007203A0', 'AK48059848A0', 'AK37072617A0', 'AK25118292A0', 'AK36058407A0', 'AK48059853A0', 'AK4A036112A0', 'AK36058192A0', 'AK49010504A0', 'AK37072801A0', 'AK37007972A0', 'AK4A036002A0', 'AK4A048829A0', 'AK49010453A0', 'AK36058402A0', 'AK37008098A0', 'AK37008114A0', 'AK49010526A0', 'AK4A022943A0', 'AK4901055A0', 'AK35062231A0', 'AK4A048830A0', 'AK49010573A0', 'AK37007216A0', 'AK37041093A0', 'AK4A048864A0', 'AK36058236A0', 'AK35062162A0', 'AK36058236A0', 'AK36058148A0', 'AK37007322A0', 'AK35062256A0', 'AK36021183A0', 'AK36058177A0', 'AK48059128A0', 'AK36058382A0', 'AK36021219A0', 'AK37007236A0', 'AK48059945A0', 'AK37007260A0', 'AK4A03611A0', 'AK59009890'],
            'OKI ES5112': ['AK89023162C0', 'AK89023875C0', 'AK89023171C0', 'AK89023873C0', 'AK89023867C0', 'AK89023222C0', 'AK89023169C0', 'AK89023869C0', 'AK89023913C0', 'AK89023212C0', 'AK48059982A0', 'AK8B014296C0', 'AK8B014406C0', 'AK89023168C0', 'AK89023161C0', 'AK89023214C0', 'AK8B015140C0', 'AK8B014306C0', 'AK8B014311C0', 'AK8B014404C0', 'AK89023868C0', 'AK89023170C0', 'AK8B035794C0', 'AK8B018386C0', 'AK89023872C0', 'AK89023164C0', 'AK8B014435C0', 'AK8B014252C0', 'AK8B007956C0', 'AK8B014307C0', 'AK89023220C0', 'AK8B014402C0', 'AK8B018310C0', 'AK89023172C0', 'AK8B008115C0', 'AK89023215C0', 'AK8B014399C0', 'AK8B014398C0', 'AK8B014280C0', 'AK0B014395C0', 'AK8B014276C0', 'AK8B014313C0', 'AK8B008054C0', 'AK8B014300C0', 'AK8B008114C0', 'AK8B008117C0', 'AK8B014432C0', 'AK89023162C0', 'AK8B014295C0', 'AK89026692C0', 'AK89023224C0', 'AK89023166C0', 'AK8B014289C0', 'AK8B008118C0', 'AK8B014442C0', 'AK8B014302C0', 'AK8B014309C0', 'AK89023902C0', 'AK8B014434C0', 'AK89023210C0', 'AK8B024324C0', 'AK8B014334C0', 'AK8B014297C0', 'AK8B014298C0', 'AK8B0114331C0', 'AK8B015147C0', 'AK8B014455C0', 'AK89023906C0', 'AK8B014450C0', 'AK8A036265C0', 'AK8B014439C0', 'AK8B014437C0', 'AK8B014290C0', 'AK8B014451C0', 'AK98005227C0', 'AK8B014282C0', 'AK8B007953C0', 'AK89023213C0', 'AK89023167C0', 'AK89023116C0', 'AK8B008116C0', 'AK8B014403C0', 'AK8B014287C0', 'AK8B035791C0', 'AK89023905C0', 'AK8B008124C0', 'AK8C031308C0', 'AK8B01544C0', 'AK89023877C0', 'AK8B014386C0'],
            'OKI ES8473': ['AL8B031226E0', 'AL86025965E0', 'AL86025955E0'],
            'HP W1030XZ': ['BRDSQBL0DC', 'BRDSQBM0BX', 'BRBSQDV0OJ'],
            'HP CF258XZ': ['CNCRQ6W3JK', 'CNCRQ6W29W'],
            'HP E77830': ['CND1M6K019'],
            'HP M479': ['BRDSQBL0DC', 'BRDSQBM0BX', 'BRBSQDV0OJ', 'CNCRQ6W3JK', 'CNCRQ6W29W'],
            'XEROX C7120/ C7125': ['SQPD131195'],
            'EPSON M04XXL': ['X3BK027922'],
            'EPSON WF-C878R': ['X6G9004077', 'X6G9004035'],
            'KYOCERA M3655IDM': ['R4P9634194'],
            'PANTUM BM5100FDW': ['CK3B007418']
        }

    def main(self):
        '''Gerencia o menu de marcas e opções.'''
        opcoes_marcas = [
            ['0', 'OKI'],
            ['1', 'HP'],
            ['2', 'XEROX'],
            ['3', 'EPSON'],
            ['4', 'KYOCERA'],
            ['5', 'PANTUM'],
            ['6', 'Sair']
        ]
        opcoes_hp = [
            ['0', 'HP W1030XZ'],
            ['1', 'HP CF258XZ'],
            ['2', 'HP E77830'],
            ['3', 'HP M479'],
            ['4', 'voltar']
        ]
        opcoes_epson = [
            ['0', 'EPSON M04XXL'],
            ['1', 'EPSON WF-C878R'],
            ['2', 'voltar']
        ]
        opcoes_xerox = [
            ['0', 'XEROX C7120/ C7125'],
            ['1', 'voltar']
        ]
        opcoes_oki = [
            ['0', 'OKI MB491'],
            ['1', 'OKI ES5112'],
            ['2', 'OKI ES8473'],
            ['3', 'voltar']
        ]
        opcoes_kyocera = [
            ['0', 'KYOCERA M3655IDM'],
            ['1', 'voltar']
        ]
        opcoes_pantum= [
            ['0', 'PANTUM BM5100FDW'],
            ['1', 'voltar']
        ]
        
        # Dicionário para mapear as impressoras coloridas
        impressoras_coloridas = ['HP E77830', 'HP M479', 'OKI ES8473', 'XEROX C7120/C7125', 'EPSON WF-C878R']
        
        while True:
            exibir_menu(opcoes_marcas)
            self.escolha_marca = obter_escolha(opcoes_marcas)

            if self.escolha_marca == 6:
                print(Fore.GREEN + 'Saindo...')
                break

            # Escolhe a lista de opções correta
            opcoes = [opcoes_oki, opcoes_hp, opcoes_xerox, opcoes_epson, opcoes_kyocera, opcoes_pantum][self.escolha_marca]
            prompt_cls()
            exibir_menu(opcoes)
            escolha = obter_escolha(opcoes)
            modelo_escolhido = opcoes[escolha][1]
            if modelo_escolhido == 'voltar':
                pass
            else:
                self.escolhas.append(modelo_escolhido)  # Adiciona o modelo escolhido
                print(f'Modelos adicionados:\n{self.escolhas}')
                
                add = input('Deseja adicionar mais algum modelo? (s/n) ').lower()
                while add not in ['s', 'n']:
                    add = input('Entrada inválida. Deseja adicionar mais algum modelo? (s/n) ').lower()
                if add != 's':
                    break
        if self.escolha_marca == 6:
            pass
        else:
            print(Fore.GREEN + 'Finalizando a solicitação:')
            print(self.escolhas)
            
            # Gerar o email de solicitação
            cumprimento = 'Bom dia!' if datetime.now().hour < 12 else 'Boa tarde!'
            self.email = f'{cumprimento}\nVenho por meio deste e-mail solicitar os modelos de toner:\n\n'
            
            for modelo in self.escolhas:
                if modelo.startswith('OKI'):
                    quantidade = '60 unidades.'
                elif modelo.startswith('HP') and modelo not in impressoras_coloridas:
                    quantidade = '15 unidades.'
                elif modelo in impressoras_coloridas:
                    quantidade = '5 kits.'  # Coloridas recebem 5 kits
                else:
                    quantidade = '5 unidades.'  # Demais impressoras também recebem 5 unidades

                numeros_serie = self.numeros_serie.get(modelo, [])
                self.email += f'{modelo} - {quantidade}\nNúmeros de Série:\n{", ".join(numeros_serie)}\n\n'
                
            print(self.email)
            
if __name__ == '__main__':
    solicitacao = SolicitacaoToner()
    solicitacao.main()
