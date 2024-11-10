import unittest  # Importa o módulo unittest para realizar testes unitários.
from selenium import webdriver  # Importa a classe webdriver do Selenium para controlar o navegador.
from selenium.webdriver.common.by import By  # Importa a classe By para localizar elementos HTML.
from selenium.webdriver.support.ui import WebDriverWait  # Importa WebDriverWait para aguardar a presença de elementos.
from selenium.webdriver.support import expected_conditions as EC  # Importa condições esperadas para interação com elementos.
import pyautogui  # Importa a biblioteca pyautogui para capturas de tela e simulação de teclado.
import time  # Importa a biblioteca time para manipulação de tempo.

    
class TesteSelenium(unittest.TestCase):  # Define uma classe de teste que herda de unittest.TestCase.

    def setUp(self):  # Método chamado antes de cada teste ser executado.
        options = webdriver.ChromeOptions()  # Cria uma instância de opções para o Chrome.
        options.add_argument("--start-maximized")  # Adiciona o argumento para iniciar o Chrome maximizado.
        self.driver = webdriver.Chrome(options=options)  # Inicializa o driver do Chrome com as opções definidas.

    def _esperar_elemento(self, by, value, timeout=10):  # Método para esperar a presença de um elemento.
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))  # Aguarda até que o elemento esteja presente.

    def _capturar(self):  # Método para tirar uma captura de tela.
        pyautogui.screenshot().save('C:/Users/rpersilv/OneDrive - NTT DATA EMEAL/Documents/GitHub/SeleniumPython/2019-selenium-java-projeto_inicial/img/'f'screenshot_{time.strftime("%Y-%m-%d_%H-%M-%S")}.png')  # Faz uma captura de tela e a salva com um timestamp no nome.

    def test_acessando_a_pagina(self):  # Método do teste principal para acessar uma página.
        self.driver.get("https://www.google.com.br")  # Abre a URL do Google.
        time.sleep(3)  # Pausa o teste por 2 segundos para permitir que a página carregue.
        self._capturar()# Captura a tela após o carregamento da página.

        try:  # Inicia um bloco de tentativa para capturar exceções.
            input_element = self._esperar_elemento(By.ID, "APjFqb")  # Espera até que o elemento de entrada esteja presente no DOM.
            input_element.send_keys("Python")  # Envia o texto "Python" para o campo de entrada.
            time.sleep(2)  # Pausa por 2 segundos para permitir que o texto seja inserido.
            self._capturar()  # Captura a tela após a inserção do texto.
            pyautogui.press('enter')  # Simula a pressão da tecla Enter.
        except Exception as e:  # Captura qualquer exceção que ocorra.
            print(f"Ocorreu um erro: {e}")  # Imprime a mensagem de erro.

        time.sleep(3)  # Pausa por 3 segundos para esperar o resultado da pesquisa.
        self._capturar()  # Captura a tela após a pesquisa.

    def tearDown(self):  # Método chamado após cada teste ser executado.
        self.driver.quit()  # Fecha o driver do navegador e encerra a sessão.

if __name__ == '__main__':  # Verifica se o script está sendo executado diretamente.
    unittest.main()  # Executa todos os testes definidos na classe de teste.