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
        time.sleep(5)
        self.driver.find_element(By.ID, "details-button").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "proceed-link").click()
        time.sleep(4)

        self.driver.find_element(By.ID, "username").send_keys("80728243")
        self.driver.find_element(By.ID, "password").send_keys("Vivo@2023!@")
        time.sleep(5)
        self.driver.find_element(By.ID, "login_button").click()

    def tearDown(self):
        # Fecha o navegador após os testes
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()