# -*- coding: utf-8 -*-

# import de la lib webdriver
from selenium import webdriver

# import sleep pour tineout
from time import sleep

# import By
from selenium.webdriver.common.by import By

# import unittest
import unittest

url = "http://blazedemo.com/"

class achatTicketTest(unittest.TestCase):

    def ouverture_navigateur(self):
        # Initie une instance ChromeDriver
        self.driver = webdriver.Chrome()

        # Ouverture lien
        self.driver.get(url)

        # Maximise la fenêtre
        self.driver.maximize_window()

        sleep(2)

    def recherche_billet(self):
        # Choix pays départ
        self.driver.find_element(By.XPATH, "//select[@name='fromPort']/option[text()='Boston']").click()

        # Chois pays déstination
        self.driver.find_element(By.XPATH, "//select[@name='toPort']/option[text()='London']").click()

        sleep(2)

        # Cherche les vols
        self.driver.find_element(By.CLASS_NAME, 'btn-primary').click()

    def choix_vol(self):
        # Prends le premier vol dans la liste
        self.driver.find_element(By.CLASS_NAME, "btn-small").click()

        sleep(2)

    def achat_billet(self):
        # Formulaire à remplire
        self.driver.find_element(By.ID, 'inputName').send_keys("John Doe")
        self.driver.find_element(By.ID, 'address').send_keys("Rue de Lutèce")
        self.driver.find_element(By.ID, 'city').send_keys("Paris")
        self.driver.find_element(By.ID, 'state').send_keys("Île-de-France")
        self.driver.find_element(By.ID, 'zipCode').send_keys("75001")
        self.driver.find_element(By.XPATH, "//select[@name='cardType']/option[text()='Visa']").click()
        self.driver.find_element(By.ID, 'creditCardNumber').send_keys("0000")
        self.driver.find_element(By.ID, 'nameOnCard').send_keys("John Doe")
        self.driver.find_element(By.ID, 'creditCardMonth').clear()
        self.driver.find_element(By.ID, 'creditCardMonth').send_keys("12")
        self.driver.find_element(By.ID, 'creditCardYear').clear()
        self.driver.find_element(By.ID, 'creditCardYear').send_keys("2025")

        sleep(5)

        # Achat du billet
        self.driver.find_element(By.CLASS_NAME, 'btn-primary').click()

    def savegarde_capture(self):
       nom = "Blazedemo_capture"
       self.driver.get_screenshot_as_file(nom + ".png")

    def capture_decran(self):
       sleep(3)
       self.savegarde_capture()

    def test_method(self):
      
       # Test ouverture navigateur #1
       self.ouverture_navigateur()

       # Test recherche billet #2
       self.recherche_billet()

       # Test choix du vol #3
       self.choix_vol()

       # Test achat billet #4
       self.achat_billet()

       # Capture résultat page finale
       self.capture_decran()

if __name__ == "__main__":
    unittest.main()



