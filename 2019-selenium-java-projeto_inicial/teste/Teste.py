from os import system
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com.br")
time.sleep(10000)
driver.quit()

    
