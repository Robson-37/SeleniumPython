import unittest
from time import sleep
from selenium import webdriver

class TesteFuncionalCN04(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # Configurações iniciais antes de todos os testes
        options = webdriver.ChromeOptions()  # Cria uma instância de opções para o Chrome.
        options.add_argument("--start-maximized")  # Adiciona o argumento para iniciar o Chrome maximizado.
        self.driver = webdriver.Chrome(options=options)  # Inicializa o driver do Chrome com as opções definidas.
        # Login no Salesforce
        sleep(5)
        self.driver.find_element_by_id("username").send_keys("<SEU_USUARIO>")
        self.driver.find_element_by_id("password").send_keys("<SUA_SENHA>")
        self.driver.find_element_by_id("Login").click()
        sleep(2)

    def test_criacao_cliente(self):
        """
        Caso de Teste 1: Criação de Cliente no Salesforce
        """
        # Acesse a seção de criação de cliente
        self.driver.find_element_by_link_text("Clientes").click()
        self.driver.find_element_by_link_text("Criar Cliente").click()
        
        # Preenchendo os detalhes do cliente
        self.driver.find_element_by_id("nome_cliente").send_keys("Cliente Teste")
        self.driver.find_element_by_id("informacoes_contato").send_keys("contato@test.com")
        self.driver.find_element_by_id("ie").send_keys("123456789")  # IE válido
        
        # Conclua a criação do cliente
        self.driver.find_element_by_id("criar_cliente").click()
        sleep(3)

        # Verificar se o cliente foi criado
        # (a lógica para verificar a criação pode variar conforme sua implementação)
        cliente_criado = self.driver.find_element_by_xpath("//*[contains(text(), 'Cliente Teste')]").is_displayed()
        self.assertTrue(cliente_criado, "O cliente não foi criado no Salesforce.")

        # Sincronização com o Vivocorp (simular sincronia)
        sleep(5)  # Esperando a sincronização acontecer
        
    def test_verificacao_sincronizacao(self):
        """
        Caso de Teste 2: Verificação da Sincronização no Vivocorp
        """
        # Acesse o Vivocorp
        self.driver.get("https://<URL_DO_VIVOCORP>")
        self.driver.find_element_by_id("username").send_keys("<SEU_USUARIO_VIVOCORP>")
        self.driver.find_element_by_id("password").send_keys("<SUA_SENHA_VIVOCORP>")
        self.driver.find_element_by_id("Login").click()
        sleep(2)

        # Busque pelo cliente recém-criado
        self.driver.find_element_by_id("campo_busca").send_keys("Cliente Teste")
        self.driver.find_element_by_id("botao_buscar").click()
        sleep(2)
        
        # Verifique se as informações estão corretas
        cliente_visivel = self.driver.find_element_by_xpath("//*[contains(text(), 'Cliente Teste')]").is_displayed()
        self.assertTrue(cliente_visivel, "O cliente não aparece nos resultados do Vivocorp.")
        
    def test_visibilidade_elementos_interface(self):
        """
        Caso de Teste 3: Visibilidade de Elementos da Interface
        """
        # Acesse a seção de criação de cliente
        self.driver.get("https://<URL_DO_SALESFORCE>/clientes/criar")
        
        # Verifique os campos obrigatórios
        campos_obrigatorios = [
            self.driver.find_element_by_id("nome_cliente").is_displayed(),
            self.driver.find_element_by_id("ie").is_displayed(),
            self.driver.find_element_by_id("endereco").is_displayed()
        ]
        
        for campo in campos_obrigatorios:
            self.assertTrue(campo, "Um dos campos obrigatórios não está visível.")

    def test_validacao_mensagem_erro(self):
        """
        Caso de Teste 4: Validação da Mensagem de Erro ao Incluir Dados Inválidos
        """
        # Acesse a seção de criação de cliente
        self.driver.get("https://<URL_DO_SALESFORCE>/clientes/criar")
        
        # Preencha os campos necessários com IE inválido
        self.driver.find_element_by_id("nome_cliente").send_keys("Cliente Teste")
        self.driver.find_element_by_id("informacoes_contato").send_keys("contato@test.com")
        self.driver.find_element_by_id("ie").send_keys("IE_INVALIDO")
        
        # Tente submeter o formulário
        self.driver.find_element_by_id("criar_cliente").click()
        sleep(2)
        
        # Verifique a mensagem de erro
        mensagem_erro = self.driver.find_element_by_id("mensagem_erro").text
        self.assertIn("IE inválido", mensagem_erro, "Mensagem de erro não foi exibida corretamente.")

    @classmethod
    def tearDownClass(cls):
        # Finaliza a sessão do navegador após todos os testes
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
