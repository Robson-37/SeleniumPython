import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestIntegracaoVivocorp(unittest.TestCase):

    def setUp(self):
        # Inicializa o driver do navegador (substitua o caminho do ChromeDriver conforme necessário)
        options = webdriver.ChromeOptions()  # Cria uma instância de opções para o Chrome.
        options.add_argument("--start-maximized")  # Adiciona o argumento para iniciar o Chrome maximizado.
        self.driver = webdriver.Chrome(options=options)

    def test_visibilidade_componentes(self):
        """Teste de Visibilidade do Componente 'Integração Vivocorp'."""
        # Passo 1: Logar no sistema SFA
        self.driver.get("https://vivo--preprod.sandbox.lightning.force.com/")
        time.sleep(10)
        self.driver.find_element(By.ID, "username").send_keys("80728243")
        self.driver.find_element(By.ID, "password").send_keys("Vivo@2023!@")
        self.driver.find_element(By.ID, "login_button").click()

        # Passo 2: Navegar até a seção de oportunidades
        self.driver.find_element(By.LINK_TEXT, "Oportunidades").click()

        # Passo 3: Selecionar uma oportunidade do tipo 5 (Novo Simplifique)
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Novo Simplifique')]").click()

        # Comportamento Esperado: Verificar a visibilidade do componente "Integração Vivocorp"
        component = self.driver.find_element(By.ID, "integracao_vivocorp")
        self.assertTrue(component.is_displayed(), "O componente 'Integração Vivocorp' não está visível na tela.")

    def test_funcionamento_botao_envio_cliente(self):
        """Teste de Funcionamento do Botão para Enviar Cliente para Vivocorp."""
        # Realizar os passos do Teste 1 para garantir que o componente está visível
        self.test_visibilidade_componentes()

        # Passo 4: Clicar no botão para enviar ou reenviar manualmente o Cliente
        enviar_botao = self.driver.find_element(By.ID, "btn_enviar_cliente")
        enviar_botao.click()

        # Comportamento Esperado: Mensagem de confirmação
        time.sleep(2)  # Esperando a mensagem aparecer
        mensagem = self.driver.find_element(By.ID, "mensagem_confirmacao").text
        self.assertEqual(mensagem, "Cliente enviado com sucesso para o Vivocorp", "A mensagem de sucesso não foi exibida.")

    def test_mensagem_sucesso_apos_envio(self):
        """Teste de Mensagem de Sucesso Após Envio."""
        self.test_funcionamento_botao_envio_cliente()  # Chamando o teste anterior que já envia o cliente

    def test_erro_envio_cliente_invalido(self):
        """Teste de Erro no Envio do Cliente."""
        # Passo 1: Logar no sistema SFA
        self.driver.get("url_do_sistema_sfa")
        self.driver.find_element(By.ID, "username").send_keys("usuario_teste")
        self.driver.find_element(By.ID, "password").send_keys("senha_teste")
        self.driver.find_element(By.ID, "login_button").click()

        # Passo 2: Navegar até a seção de oportunidades
        self.driver.find_element(By.LINK_TEXT, "Oportunidades").click()

        # Passo 3: Selecionar uma oportunidade do tipo 5 (Novo Simplifique)
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Novo Simplifique')]").click()

        # Tentar enviar um cliente inválido
        enviar_botao = self.driver.find_element(By.ID, "btn_enviar_cliente_invalido")
        enviar_botao.click()

        # Comportamento Esperado: Mostrar mensagem de erro
        time.sleep(2)  # Esperando a mensagem aparecer
        mensagem = self.driver.find_element(By.ID, "mensagem_erro").text
        self.assertEqual(mensagem, "Erro: Cliente não pode ser enviado", "A mensagem de erro não foi exibida.")

    def test_persistencia_dados(self):
        """Teste de Persistência de Dados."""
        self.test_funcionamento_botao_envio_cliente()  # Garantir que o cliente foi enviado

        # Acessar o sistema Vivocorp para verificar dados do cliente
        self.driver.get("http://vivocorp-preprod-qa.redecorp.br/vivocorp_oui")
        # Aqui você precisaria adicionar o código para garantir que verificar os dados no Vivocorp
        # Exemplo:
        # cliente_dados = self.driver.find_element(By.XPATH, "//table[contains(@class, 'clientes')]")
        # self.assertTrue(cliente_dados)

    def tearDown(self):
        # Fecha o navegador após os testes
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
