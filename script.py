# -*- coding: utf-8 -*-

# import de la lib webdriver
from selenium import webdriver

# import sleep pour tineout
from time import sleep

# import By
from selenium.webdriver.common.by import By

url = "http://blazedemo.com/"

# Initie une instance ChromeDriver
driver = webdriver.Chrome()

# Ouverture lien
driver.get(url)

# Maximise la fenêtre
driver.maximize_window()

sleep(2)

# Choix pays départ
driver.find_element(By.XPATH, "//select[@name='fromPort']/option[text()='Boston']").click()

# Chois pays déstination
driver.find_element(By.XPATH, "//select[@name='toPort']/option[text()='London']").click()

# Cherche les vols
driver.find_element(By.CLASS_NAME, 'btn-primary').click()

sleep(2)

# Prends le premier vol dans la liste
driver.find_element(By.CLASS_NAME, "btn-small").click()

sleep(2)

# Formulaire à remplire
driver.find_element(By.ID, 'inputName').send_keys("John Doe")
driver.find_element(By.ID, 'address').send_keys("Rue de Lutèce")
driver.find_element(By.ID, 'city').send_keys("Paris")
driver.find_element(By.ID, 'state').send_keys("Île-de-France")
driver.find_element(By.ID, 'zipCode').send_keys("75001")
driver.find_element(By.XPATH, "//select[@name='cardType']/option[text()='Visa']").click()
driver.find_element(By.ID, 'creditCardNumber').send_keys("0000")
driver.find_element(By.ID, 'nameOnCard').send_keys("John Doe")
driver.find_element(By.ID, 'creditCardMonth').send_keys("12")
driver.find_element(By.ID, 'creditCardYear').send_keys("2025")

sleep(5)

# Achat du billet
driver.find_element(By.CLASS_NAME, 'btn-primary').click()

sleep(15)

def savegarde_capture():
    nom = "Blazedemo_capture"
    driver.get_screenshot_as_file(nom + ".png")

savegarde_capture()

driver.quit()