# -*- coding: utf-8 -*-

# import de la lib webdriver
from selenium import webdriver

# import sleep pour tineout
from time import sleep

url = "http://blazedemo.com/index.php"

# Initie une instance ChromeDriver
driver = webdriver.Chrome()

# Ouverture lien
driver.get(url)

# Maximise la fenêtre
driver.maximize_window()
