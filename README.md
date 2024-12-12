# 🤖 Automação de Chamados e Gestão de Tabelas 🤖

Este projeto é um web scraper desenvolvido em Python que automatizam processos internos de abertura de chamados e gestão de dados na empresa. Os scripts estão organizados em três diretórios principais:

- `pc_monitor`
- `impressora`
- `db_tables`

**Importante:** Algumas informações sensíveis, como números de telefone e e-mails, foram removidas do código por questões de privacidade. Além disso, o login e a senha utilizados no sistema são armazenados através de variáveis de ambiente no computador, que são ensinadas a fazer no final.

## Estrutura do Repositório 🗂️
### 1. `pc_monitor` 🖥️

Este módulo é responsável pela abertura de chamados para conserto de computadores. Ele automatiza o preenchimento de formulários na intranet da empresa e registra as informações em um banco de dados local.

#### Funcionalidades:
- Automação com Selenium: Realiza login e navegação em um sistema interno, preenchendo formulários com dados fornecidos pelo usuário.  
- Coleta de Dados: O menu interativo solicita informações como patrimônio, host, marca, localização e descrição do problema.  
- Banco de Dados SQLite: Salva os chamados registrados localmente para consulta futura.  

#### Componentes principais
1- App.py
  - Inicializa o WebDriver e configura a automação.
  - Coleta informações do terminal por meio da classe Solicitacao.
  - Insere os dados no sistema interno e os registra no banco de dados.

2- database.py  
  - Gerencia o banco de dados SQLite, criando a tabela Pc_Monitor e inserindo dados dos chamados.

3- menu.py
  - Contém a lógica do menu interativo para entrada de dados do usuário.

4- setup.py
  - Configura o empacotamento do aplicativo com o cx_Freeze para distribuição.


#### Objetivo:
Agilizar o processo de abertura de chamados e garantir o registro seguro e acessível das informações.

### 2. `impressora` 🖨️

Este módulo é responsável por automatizar a solicitações de toner para impressoras.

#### Funcionalidades:
- Exibe uma tabela contendo marcas e modelos de impressoras disponíveis na empresa.
- Permite ao usuário selecionar o modelo desejado e faz a solicitação automaticamente.
- Registra informações no banco de dados local, incluindo:
  - Data de abertura do chamado
  - O que foi solicitado
  - Quantidade solicitada

#### Objetivo:
Facilitar a solicitação de toner e manter o histórico de pedidos organizado.

### 3. `db_tables` 📅

Gerencia os dados armazenados no banco de dados.

#### Funcionalidades:
- Exibe tabelas disponíveis:
  - Tabela de chamados para computadores
  - Tabela de solicitação de toner
- Permite interações específicas com a tabela de chamados para computadores:
  - Adicionar data de ida
  - Adicionar data de volta
  - Adicionar data de entrega
  - Excluir linhas específicas

#### Objetivo:
Garantir a manutenção e a acessibilidade das informações armazenadas.

## Tecnologias Utilizadas 👨‍💻

- **Linguagem**: Python
- **Banco de Dados**: SQLite
- **Ambiente de Execução**: Scripts executados em ambiente local
- **Privacidade**: Informações sensíveis (e-mails e telefones) foram censuradas. Login e senha são gerenciados por variáveis de ambiente.

## Configuração e Execução ⚙️

### 1. Configurando Variáveis de Ambiente 

Para o correto funcionamento dos scripts, é necessário configurar as seguintes variáveis de ambiente:

- `GANET_USER`: Usuário do sistema GANET.
- `GANET_PASSWORD`: Senha do sistema GANET.
- `WEBMAIL_EMAIL`: Endereço de e-mail usado no sistema.
- `WEBMAIL_PASSWORD`: Senha do e-mail configurado.

#### **Windows**

1. Pressione `Win + R`, digite `SystemPropertiesAdvanced` e clique em OK.
2. Clique no botão **Variáveis de Ambiente**.
3. Na seção **Variáveis do Sistema**, clique em **Novo**.
4. Adicione o nome e valor das variáveis:
   - Nome: `GANET_USER`, Valor: `seu_usuário_ganet`
   - Nome: `GANET_PASSWORD`, Valor: `sua_senha_ganet`
   - Nome: `WEBMAIL_EMAIL`, Valor: `seu_email_webmail`
   - Nome: `WEBMAIL_PASSWORD`, Valor: `sua_senha_webmail`
5. Clique em **OK** para salvar e fechar.

#### **Linux/MacOS**

1. Abra o terminal e edite o arquivo de configuração do shell, como `~/.bashrc` ou `~/.zshrc`, adicionando:

   ```bash
   export GANET_USER="seu_usuário_ganet"
   export GANET_PASSWORD="sua_senha_ganet"
   export WEBMAIL_EMAIL="seu_email_webmail"
   export WEBMAIL_PASSWORD="sua_senha_webmail"
