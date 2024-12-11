from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep
import os
from menu import Solicitacao
from database import DataBase

def start_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--start-maximized', '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': 'C:\\Users\\secretario',
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(options=chrome_options)

    return driver

def wait_for_element(driver, by, value, timeout=60):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )

# Infos
user = os.getenv('GANET_USER')
password = os.getenv('GANET_PASSWORD')

# Infos do Usuário
info = Solicitacao()
info.main()


def main():
    driver = None
    try:
        driver = start_driver()
        driver.get('http://172.16.0.4/')

        # Login
        wait_for_element(driver, By.ID, 'TextBox1').send_keys(user)
        driver.find_element(By.ID, 'TextBox2').send_keys(password)
        cod = driver.find_element(By.ID, 'Label2').text
        driver.find_element(By.ID, 'TextBox3').send_keys(cod)
        driver.find_element(By.ID, 'Button1').click()

        # Navegando e preenchendo o formulário
        wait_for_element(driver, By.ID, 'ctl00_GridView1_ctl04_HyperLink8').click()
        wait_for_element(driver, By.XPATH, '//a[text()="Solicitação de Serviços"]').click()
        wait_for_element(driver, By.ID, 'ctl00_ContentPlaceHolder1_btnHide').click()
        
        # Preenchendo o cadastro
        Select(driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$ddl_servico')).select_by_index(4)
        driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_txt_endereco').send_keys('XXXXXXXX')
        driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_txt_ramal').send_keys('(XX)XXXXX-XXXXX')
        driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_txt_descricao').send_keys(info.data['descrição'] + ' - ' + info.data['local'])
        driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$imb_cadastrar').click()
        sleep(0.2)
        driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$imb_cadastrar').click()

        # Cadastro parte 2
        for value in info.all_data:
            wait_for_element(driver, By.ID, 'ctl00_ContentPlaceHolder1_txt_patrimonio').send_keys(value['patrimonio'])
            if value.get('host'):
                driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_txt_etiqueta').send_keys(value['host'])
            driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_txt_marca').send_keys(value['marca'])
            driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_btn_gravar').click()
        
        print('Fechando o navegador...')
        driver.quit()

        print('Adicionando ao Banco de Dados...')
        db= DataBase('C:\\database\\chamado_info.db')
        for value in info.all_data:
            db.add(value['local'], value['patrimonio'], value['host'])
        print('\nAdicionado ao Banco de Dados :)\n')

        
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
    finally:
        # Fechando o webdriver
        try:
            if driver:
                driver.quit()
        except Exception as e:
            print(f'Erro ao fechar o WebDriver: {e}')
        
        print('Programa finalizado')

if __name__ == '__main__':
    main()
