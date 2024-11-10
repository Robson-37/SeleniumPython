import unittest  # Importa o módulo unittest para criar e executar testes
from selenium import webdriver  # Importa o módulo webdriver do Selenium para automação de navegadores
from selenium.webdriver.common.keys import Keys  # Importa as chaves do teclado do Selenium
from selenium.webdriver.common.by import By  # Importa a classe By para localizar elementos
from selenium.webdriver.support.ui import WebDriverWait  # Importa WebDriverWait para esperar por elementos
from selenium.webdriver.support import expected_conditions as EC  # Importa condições esperadas para verificar elementos
import time  # Importa o módulo time para manipulação de tempo
import pyautogui  # Importa a biblioteca pyautogui para controle da interface gráfica
import pyscreeze  # Importa a biblioteca pyscreeze, útil para capturas de tela

class TesteSelenium(unittest.TestCase):  # Define a classe de teste como uma subclasse de unittest.TestCase
    def setUp(self):  # Método que será executado antes de cada teste
        options = webdriver.ChromeOptions()  # Cria um objeto de opções para o Chrome
        options.add_argument("--start-maximized")  # Adiciona argumento para iniciar o Chrome maximizado
        self.driver = webdriver.Chrome(options=options)  # Inicializa o driver do Chrome com as opções definidas
    
    def test_acessando_a_pagina(self):  # Método de teste para acessar a página
        self.driver.get("https://www.google.com.br")  # Abre a URL do Google no navegador
        time.sleep(2)  # Pausa por 2 segundos para garantir que a página carregue
        self.capturar()  # Chama o método para capturar a tela
        #self.assertIn("Google", self.driver.title)  # Verifica se "Google" está no título da página
        #WebDriverWait(self.driver, 10).until(EC.title_contains("Google"))  # Espera até que o título contenha "Google"
        
        try:  # Inicia um bloco de exceção para capturar erros
            # Espera até que o elemento com ID "APjFqb" esteja presente no DOM
            input_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "APjFqb")))  # Localiza o elemento pelo ID "APjFqb"

            # Agora podemos interagir com o elemento
            input_element.send_keys("Python")  # Envia a palavra "Python" para o campo de entrada
            time.sleep(2)  # Pausa por 2 segundos
            self.capturar()  # Captura a tela novamente
            pyautogui.press('enter')  # Pressiona a tecla 'Enter' usando pyautogui

        except Exception as e:  # Captura qualquer exceção ocorrida
            print(f"Ocorreu um erro: {e}")  # Imprime a mensagem de erro no console
    
        time.sleep(3)  # Pausa por 3 segundos antes de capturar a tela novamente
        self.capturar()  # Captura a tela uma última vez


    def capturar(self):  # Método para capturar a tela
        self.capimagem = pyautogui.screenshot()  # Captura a tela atual
        # Salva a captura de tela com um nome que inclui a data e hora atuais
        self.capimagem.save('C:/Users/rpersilv/OneDrive - NTT DATA EMEAL/Documents/GitHub/SeleniumPython/2019-selenium-java-projeto_inicial/img/'f'screenshot_{time.strftime("%Y-%m-%d_%H-%M-%S")}.png') 

    def tearDown(self):  # Método que será executado após cada teste
        self.driver.quit()  # Fecha o navegador e encerra a sessão do driver

if __name__=='__main__':  # Verifica se o arquivo é executado como programa principal
    unittest.main()  # Executa os testes definidos na classe