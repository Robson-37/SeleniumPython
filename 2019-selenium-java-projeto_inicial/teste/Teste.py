
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Correção: Keys com 'K' maiúsculo
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


try:
    # Inicializa o driver do Chrome
    driver = webdriver.Chrome()
    # Abre o site do Google
    driver.get("https://www.google.com.br")
    
    # Aguarda até que um elemento específico esteja presente na página (exemplo: o campo de pesquisa)
    # Aqui estamos usando o título da página como condição para a espera.
    # WebDriverWait(driver, 10000).until(EC.title_contains("Google"))
    time.sleep(500)
    
    # Adicione uma lógica adicional aqui, se necessário.
    
finally:
    # Garante que o driver será fechado
    driver.quit()


    
