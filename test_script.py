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

        sleep(3)


    def test_method(self):
      
       # Test step #1
       self.ouverture_navigateur()

       # Test step #2
       self.recherche_billet()

       # Test step #3
       self.choix_vol()


if __name__ == "__main__":
    unittest.main()



