import unittest  # Importa o módulo unittest para realizar testes unitários.
from selenium import webdriver  # Importa a classe webdriver do Selenium para controlar o navegador.
from selenium.webdriver.common.by import By  # Importa a classe By para localizar elementos HTML.
from selenium.webdriver.support.ui import WebDriverWait  # Importa WebDriverWait para aguardar a presença de elementos.
from selenium.webdriver.support import expected_conditions as EC  # Importa condições esperadas para interação com elementos.
import pyautogui  # Importa a biblioteca pyautogui para capturas de tela e simulação de teclado.
import time  # Importa a biblioteca time para manipulação de tempo.

class CriarCliente(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

    def _esperar_elemento(self, by, value, timeout=10):  # Método para esperar a presença de um elemento.
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))  # Aguarda até que o elemento esteja presente.
    
    def test_acesso_a_simplifique(self):
        self.driver.get("https://simalog2.simplifiquevivoemp.com.br/")
        time.sleep(15)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

