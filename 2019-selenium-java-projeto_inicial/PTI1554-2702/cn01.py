# Classe de Teste Automatizada em Python

# Abaixo segue uma classe de testes automatizados que implementa os casos de teste manuais fornecidos. Esta classe utiliza o framework #   Selenium para interagir com a interface da web e realizar as validações necessárias. Certifique-se de ter o Selenium instalado e um driver apropriado para o navegador que pretende usar.


from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TesteIntegracaoVivocorp(unittest.TestCase):

    def setUp(self):
        # Inicializa o driver do Selenium
        options = webdriver.ChromeOptions()  # Cria uma instância de opções para o Chrome.
        options.add_argument("--start-maximized")  # Adiciona o argumento para iniciar o Chrome maximizado.
        self.driver = webdriver.Chrome(options=options)  # Método para realizar o login
        time.sleep(5)

    def login(self):
        # Lógica de login (substitua pelos seletores corretos)
        self.driver.find_element(By.NAME, "username").send_keys("SEU_USUARIO")
        self.driver.find_element(By.NAME, "password").send_keys("SUA_SENHA")
        self.driver.find_element(By.NAME, "login").click()  # Botão de login

        # Aguarda 2 segundos para garantir que a página carregue
        time.sleep(10)

    def test_visibilidade_componente_integration_vivocorp(self):
        # Cenário: Acessa a seção de Oportunidades e verifica o componente "Integração Vivocorp"
        self.driver.find_element(By.LINK_TEXT, "Oportunidades").click()  # Navegando para Oportunidades
        self.driver.find_element(By.LINK_TEXT, "Novo Simplifique").click()  # Selecionando a oportunidade tipo 5

        # Verifica se o componente está visível
        vivocorp_component = self.driver.find_element(By.ID, "vivocorp-component")
        self.assertTrue(vivocorp_component.is_displayed(), "O componente 'Integração Vivocorp' não está visível.")

    def test_funcionalidade_botao_enviar_reenviar_cliente(self):
        # Cenário: Enviar/reenviar cliente através do componente
        vivocorp_component = self.driver.find_element(By.ID, "vivocorp-component")
        self.assertTrue(vivocorp_component.is_enabled(), "O componente 'Integração Vivocorp' não está habilitado.")
        
        botao_enviar = self.driver.find_element(By.ID, "botao-enviar")
        botao_enviar.click()  # Clicar no botão enviar

        # Verifica mensagem de sucesso
        mensagem = self.driver.find_element(By.ID, "mensagem-sucesso").text
        self.assertEqual(mensagem, "Envio foi bem-sucedido.", "Mensagem de envio não foi exibida corretamente.")

    def test_mensagem_erro_envio_cliente_sem_dados(self):
        # Cenário: Tenta enviar um cliente sem preencher os dados obrigatórios
        botao_enviar = self.driver.find_element(By.ID, "botao-enviar")
        botao_enviar.click()  # Clica no botão sem preencher dados

        # Verifica mensagem de erro
        mensagem_erro = self.driver.find_element(By.ID, "mensagem-erro").text
        self.assertEqual(mensagem_erro, "Dados obrigatórios para o envio são necessários.", "Mensagem de erro não foi exibida corretamente.")

    def test_inatividade_botao_sem_acesso(self):
        # Cenário: Verifica que o botão está desabilitado se o usuário não tem acesso
        botao_enviar = self.driver.find_element(By.ID, "botao-enviar")
        self.assertFalse(botao_enviar.is_enabled(), "O botão de enviar/reeenviar deve estar desabilitado.")

    def test_comportamento_sistema_reenviar_cliente(self):
        # Cenário: Tenta reenviar um cliente já enviado
        botao_reenviar = self.driver.find_element(By.ID, "botao-reenviar")
        botao_reenviar.click()  # Clica no botão reenviar

        # Verifica mensagem que cliente já foi enviado
        mensagem = self.driver.find_element(By.ID, "mensagem-informativa").text
        self.assertEqual(mensagem, "O cliente já foi enviado anteriormente e não pode ser reenviado.", "Mensagem de reenviar não foi exibida corretamente.")

    def tearDown(self):
        # Fecha o driver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


#=============================================================================================================================================

# Text
### Notas Importantes

#- **Substitua `URL_DA_SUA_APLICACAO`**: Você deve inserir a URL correta da aplicação que está sendo testada.
#- **Alterar Seletores**: Os seletores de elementos (como IDs e nomes) devem ser ajustados conforme a estrutura real da sua aplicação.
#- **Dependências**: Para executar este código, você vai precisar das bibliotecas `selenium` e `unittest`, além do driver do Selenium adequado ao seu navegador (ex: ChromeDriver).
  
#Sinta-se à vontade para adaptar o código conforme necessário para atender aos requisitos específicos do seu ambiente de testes.
