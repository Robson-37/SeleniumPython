import unittest
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

def tira_print(imagem: str ='..//img//print.png'):

        try:
            captura = pyautogui.screenshot()
            captura.save(imagem)
            print(f'Print salvo como {imagem}')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

class TesteSelenium(unittest.TestCase):

    def setUp(self):
        # Inicializa o driver do Chrome
        options = webdriver.ChromeOptions()
        
        # Maximizar a janela do navegador
        
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

    def test_google_search(self):

        driver = self.driver
        driver.get("https://www.google.com.br")
        tira_print()
        # Aguarda até que o título da página contenha "Google"
        time.sleep(5)
 
        # Você pode adicionar mais lógica aqui para interagir com a página
        #print("Página carregada corretamente")

    def tearDown(self):
        # Garante que o driver será fechado
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
