# Classe de Teste Automatizado em Python para Requisitos CN03

## Pré-requisitos
#Antes de executar os testes, certifique-se de que você possui as seguintes bibliotecas instaladas:
#- `selenium` (para automação de browser)
#- `unittest` (para estruturação dos testes)
#- `pandas` (opcional, se precisar manipular arquivos CSV)

## Classe de Teste

# python

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TesteCriacaoClientesEmMassa(unittest.TestCase):

    def setUp(self):
        # Configuração do WebDriver
        options = webdriver.ChromeOptions()  # Cria uma instância de opções para o Chrome.
        options.add_argument("--start-maximized")  # Adiciona o argumento para iniciar o Chrome maximizado.
        self.driver = webdriver.Chrome(options=options)  # Inicializa o driver do Chrome com as opções definidas.
        time.sleep(5)
        self.login()  # Chamada para o método de login

    def login(self):
        # Lógica para logar no Salesforce
        usuario = self.driver.find_element(By.ID, 'input_usuario')
        senha = self.driver.find_element(By.ID, 'input_senha')
        usuario.send_keys('SEU_USUARIO')
        senha.send_keys('SUA_SENHA')
        senha.submit()

    def test_criacao_clientes_em_massa(self):
        # Teste para criação de clientes em massa
        self.driver.find_element(By.ID, 'link_carga_clientes').click()  # Acessar carga de clientes
        self.driver.find_element(By.ID, 'input_arquivo').send_keys('CAMINHO_PARA_O_ARQUIVO_DE_CLIENTES')  # Inserir caminho do arquivo
        self.driver.find_element(By.ID, 'botao_iniciar_carga').click()  # Iniciar carga
        time.sleep(5)  # Espera a carga para que o sistema responda

        # Verifica se a carga foi bem-sucedida
        self.clientes_criados = self.driver.find_elements(By.CLASS_NAME, 'cliente_criado')  # Exemplo de classe para clientes criados
        self.assertGreater(len(self.clientes_criados), 0, "Nenhum cliente foi criado.")

        # Verificar sincronização com Vivocorp
        self.verificar_sincronizacao_vivocorp()

    def verificar_sincronizacao_vivocorp(self):
        # Método que deve verificar a sincronização no Vivocorp
        self.driver.get('URL_DO_VIVOCORP')  # Insira a URL do Vivocorp
        # Lógica para autenticação no Vivocorp semelhante a do Salesforce
        # ...

        # Verificando clientes no Vivocorp
        for cliente in self.clientes_criados:  # Loop sobre os clientes criados
            # A logica de busca e verificação de clientes e seus dados vai aqui
            # Exemplo de verificação
            self.assertIn(cliente.text, self.driver.page_source, "Cliente não encontrado no Vivocorp.")

    def test_verificacao_visibilidade_botao_cadastro_cliente(self):
        # Teste para verificar a visibilidade do botão de criar cliente em massa
        self.driver.get('URL_DO_SALESFORCE')
        self.assertTrue(self.driver.find_element(By.ID, 'botao_criar_cliente_massa').is_displayed(), "Botão 'Criar Cliente em Massa' não está visível.")

    def test_verificacao_visibilidade_botao_sincronizacao(self):
        # Teste para verificar a visibilidade do botão de sincronização
        self.driver.get('URL_DO_SALESFORCE')
        # Assumir que a carga foi realizada anteriormente
        self.assertTrue(self.driver.find_element(By.ID, 'botao_sincronizar_vivocorp').is_displayed(), "Botão 'Sincronizar com Vivocorp' não está visível.")

    def tearDown(self):
        # Fechar o navegador após os testes
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
#text
## Instruções de Execução
#1. **Substitua** os espaços reservados nas URLs, IDs de elementos e credenciais para refletir seu ambiente de teste real.
#2. **Execute** o script em seu ambiente Python com as bibliotecas necessárias instaladas.
#3. **Verifique** os logs e resultados finais de cada teste.
