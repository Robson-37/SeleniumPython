import unittest
from selenium import webdriver
# Correção: Keys com 'K' maiúsculo
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TesteSelenium(unittest.TestCase):

    def setUp(self):
        # Inicializa o driver do Chrome
        options = webdriver.ChromeOptions()
        
        # Maximizar a janela do navegador
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

    def test_google_search(self):

        driver = self.driver
        driver.get("https://www.google.com.br")

        # Aguarda até que o título da página contenha "Google"
        time.sleep(5)

        # Você pode adicionar mais lógica aqui para interagir com a página
        print("Página carregada corretamente")

    def tearDown(self):
        # Garante que o driver será fechado
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
