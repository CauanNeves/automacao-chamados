'''
Essa é uma versão para fins de estudo, ainda não está completa e tem muito o que ajustar.
Nesse primeiro momento a base já está feita.
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
from menu import SolicitacaoToner
from database import DataBase


def start_driver():
    chromeOptions= Options()
    arguments= ['--lang=pt-BR', '--start-maximized', '--incognito']

    for argument in arguments:
        chromeOptions.add_argument(argument)
    
    chromeOptions.add_experimental_option('prefs', {
    'download.default_directory': 'C:\\Users\\secretario',
    'download.directory_upgrade': True,
    'download.prompt_for_download': False,
    'profile.default_content_setting_values.notfications': 2,
    'profile.default_content_setting_values.automatic_downloads': 1,
    
    })

    driver= webdriver.Chrome(options=chromeOptions)   

    return driver

def wait_for_element(driver, by, value, timeout=60):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )

# Infos
email = os.getenv('WEBMAIL_EMAIL')
password = os.getenv('WEBMAIL_PASSWORD')

datas= SolicitacaoToner()
datas.main()

def main():
    if datas.escolha_marca == 6:
        pass
    else:
        driver = start_driver()
        driver.get('https://webmail.angra.rj.gov.br/webmail/')

        try:
            #Email
            wait_for_element(driver, By.NAME, 'email-address').send_keys(email)
            driver.find_element(By.NAME, 'next').click()

            #Senha
            wait_for_element(driver, By.NAME, 'password').send_keys(password)
            driver.find_element(By.NAME, 'next').click()

            # Aguardar até que a página principal esteja carregada e elementos estejam visíveis
            wait_for_element(driver, By.ID, 'gui.frm_main.new#main').click()
            wait_for_element(driver, By.ID, 'gui.frm_new_item#mail').click()

            # Compor o email
            element = driver.find_element(By.ID, 'gui.frm_compose.to.plus#main')

            element.send_keys('XXX@XXXX.com.br, XXXXX@gmail.com', Keys.TAB, 'Solicitação de Toner')
            sleep(1)

            #Encontrando e colocando o selenium para atuar no iframe
            iframe= driver.find_element(By.XPATH, '//iframe[@src= "about:blank"]')
            driver.switch_to.frame(iframe)

            #Preenchendo email
            driver.find_element(By.XPATH, '//div').send_keys(datas.email)
            sleep(0.2)

            #saindo do iframe
            driver.switch_to.default_content()
            sleep(0.2)

            driver.find_element(By.ID, 'gui.frm_compose.x_btn_send#main').click()
            sleep(10)

            driver.quit()

            print('\nSolicitação feita com sucesso!\n')

            print('Adicionando ao Banco de Dados...')
            db= DataBase('C:\\database\\chamado_info.db')
            for value in datas.escolhas:
                if value.startswith('OKI'):
                    quantidade = '60 unidades.'
                elif value.startswith('HP') and value not in ['HP E77830', 'HP M479', 'OKI ES8473', 'XEROX C7120/C7125', 'EPSON WF-C878R']:
                    quantidade = '10 unidades.'
                elif value in ['HP E77830', 'HP M479', 'OKI ES8473', 'XEROX C7120/C7125', 'EPSON WF-C878R']:
                    quantidade = '5 kits.'  # Coloridas recebem 5 kits
                else:
                    quantidade = '5 unidades.'  # Demais impressoras também recebem 5 unidades
                db.add(marca= value.split()[0], modelo= value.split()[1], quantidade= quantidade)
            print('Adicionado ao Banco de Dados: )\n')

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        finally:
            try:
                if driver:
                    driver.quit()
            except Exception as e:
                print(f'Erro ao fechar o WebDriver: {e}')
            print('Programa Finalizado!')
            sleep(1)

if __name__ == '__main__':
    main()