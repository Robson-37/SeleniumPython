import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import pyscreeze

class TesteSelenium(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
    
    def test_acessando_a_pagina(self):
        self.driver.get("https://www.google.com.br")
        time.sleep(2)
        self.capturar()
        #self.assertIn("Google", self.driver.title)  # Verifica se "Google" está no título da página
        #WebDriverWait(self.driver, 10).until(EC.title_contains("Google"))
        
        try:
            # Espera até que o elemento esteja presente no DOM
            input_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "APjFqb")))

            # Agora podemos interagir com o elemento
            input_element.send_keys("Python")
            time.sleep(2)
            self.capturar()
            pyautogui.press('enter')    

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    
        time.sleep(3)
        self.capturar()


    def capturar(self):

        self.capimagem = pyautogui.screenshot()
        self.capimagem.save('C:/Users/rpersilv/OneDrive - NTT DATA EMEAL/Documents/GitHub/SeleniumPython/2019-selenium-java-projeto_inicial/img/'f'screenshot_{time.strftime("%Y-%m-%d_%H-%M-%S")}.png')

    def tearDown(self):
        self.driver.quit()   

if __name__=='__main__':
    unittest.main()
