import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TesteCriacaoCliente:
    def __init__(self):
        # Inicializa o web driver
        options = webdriver.ChromeOptions()  # Cria uma instância de opções para o Chrome.
        options.add_argument("--start-maximized")  # Adiciona o argumento para iniciar o Chrome maximizado.
        self.driver = webdriver.Chrome(options=options)  # Inicializa o driver do Chrome com as opções definidas.

    def test_criacao_cliente_por_converter_lead(self):
        """Caso de Teste 1 - Verificar Criação de Cliente ao Converter Lead em Oportunidade"""
        self.driver.get("URL_DO_SALESFORCE")

        # Acesse a tela de leads e faça login
        self.login_sucesso()

        # Seleciona o lead desejado
        self.driver.find_element(By.LINK_TEXT, "Leads").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Lead desejado')]").click()

        # Converter Lead
        self.driver.find_element(By.LINK_TEXT, "Converter Lead").click()
        self.driver.find_element(By.NAME, "campo_ie").send_keys("123456789") # Preencha IE
        self.driver.find_element(By.NAME, "Criar Oportunidade").click()

        # Comportamento Esperado
        novo_cliente = self.driver.find_element(By.XPATH, "//h1[contains(text(),'Cliente Criado')]")
        assert novo_cliente is not None, "O cliente não foi criado."

    def test_sincronizacao_cliente_vivocorp(self):
        """Caso de Teste 2 - Verificar Sincronização do Cliente com Vivocorp"""
        self.driver.get("URL_DA_VIVOCORP")

        # Pesquisar cliente
        self.driver.find_element(By.NAME, "search").send_keys("Nome do Cliente")
        self.driver.find_element(By.NAME, "btn_search").click()

        # Comportamento Esperado
        cliente_encontrado = self.driver.find_element(By.XPATH, "//div[contains(text(),'Nome do Cliente')]")
        assert cliente_encontrado is not None, "Cliente não encontrado no Vivocorp."

    def test_sincronizacao_contatos_relacionados(self):
        """Caso de Teste 3 - Verificar Sincronização de Contatos Relacionados"""
        self.driver.get("URL_DA_VIVOCORP")

        # Pesquisar cliente
        self.driver.find_element(By.NAME, "search").send_keys("Nome do Cliente")
        self.driver.find_element(By.NAME, "btn_search").click()

        # Verificar contatos relacionados
        relatorios_contatos = self.driver.find_element(By.ID, "contatos_relacionados")
        assert relatorios_contatos is not None and len(relatorios_contatos.find_elements_by_tag_name("li")) > 0, "Contatos relacionados não encontrados."

    def test_informacoes_endereco_vivocorp(self):
        """Caso de Teste 4 - Verificar Informações do Endereço no Vivocorp"""
        self.driver.get("URL_DA_VIVOCORP")

        # Pesquisar cliente
        self.driver.find_element(By.NAME, "search").send_keys("Nome do Cliente")
        self.driver.find_element(By.NAME, "btn_search").click()

        # Verificar informações de endereço
        endereco_cliente = self.driver.find_element(By.ID, "endereco_cliente")
        assert endereco_cliente is not None, "Informações de endereço não correspondem ao Salesforce."

    def test_elementos_interface_usuario(self):
        """Caso de Teste 5 - Verificar Elementos da Interface do Usuário"""
        self.driver.get("URL_DO_SALESFORCE")

        # Navega até a tela de criação de cliente
        self.login_sucesso()
        self.driver.find_element(By.LINK_TEXT, "Criar Cliente").click()

        # Verificar visibilidade dos elementos
        assert self.driver.find_element(By.NAME, "Nome do Cliente").is_displayed(), "Campo 'Nome do Cliente' não está visível."
        assert self.driver.find_element(By.NAME, "Endereço").is_displayed(), "Campo 'Endereço' não está visível."
        assert self.driver.find_element(By.NAME, "Salvar").is_displayed(), "Botão 'Salvar' não está visível."

    def login_sucesso(self):
        """Método auxiliar para realizar login no Salesforce"""
        self.driver.find_element(By.NAME, "username").send_keys("SEU_USUARIO")
        self.driver.find_element(By.NAME, "password").send_keys("SUA_SENHA")
        self.driver.find_element(By.NAME, "Login").click()
        time.sleep(3)

    def fechar(self):
        """Fecha o navegador após os testes"""
        self.driver.quit()

if __name__ == "__main__":
    teste = TesteCriacaoCliente()
    teste.test_criacao_cliente_por_converter_lead()
    teste.test_sincronizacao_cliente_vivocorp()
    teste.test_sincronizacao_contatos_relacionados()
    teste.test_informacoes_endereco_vivocorp()
    teste.test_elementos_interface_usuario()
    teste.fechar()
