import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_Login_Positive(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com") # buka situs
        driver.find_element(By.ID, "user-name").send_keys("standard_user") # isi email
        driver.find_element(By.ID, "password").send_keys("secret_sauce") # isi password
        driver.find_element(By.ID,"login-button").click() # masuk

    def test_Login_Usernameinvalid(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com")# buka situs
        driver.find_element(By.ID, "user-name").send_keys("standard") # isi email
        driver.find_element(By.ID, "password").send_keys("secret_sauce") # isi password
        driver.find_element(By.ID,"login-button").click() # masuk

    def test_Login_Passwordinvalid(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com")# buka situs
        driver.find_element(By.ID, "user-name").send_keys("standard_user") # isi email
        driver.find_element(By.ID, "password").send_keys("secret_ sauce") # isi password
        driver.find_element(By.ID,"login-button").click() # masuk    

    def test_Adding_carts_success(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com") # buka situs
        driver.find_element(By.ID, "user-name").send_keys("standard_user") # isi email
        driver.find_element(By.ID, "password").send_keys("secret_sauce") # isi password
        driver.find_element(By.ID,"login-button").click() # masuk
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click() #add to cart
        driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click() #add to cart

    def test_Checkout_success(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com") # buka situs
        driver.find_element(By.ID, "user-name").send_keys("standard_user") # isi email
        driver.find_element(By.ID, "password").send_keys("secret_sauce") # isi password
        driver.find_element(By.ID,"login-button").click() # masuk
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click() #add to cart
        driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click() #add to cart
        driver.find_element(By.ID,"shopping_cart_container").click() # buka keranjang
        driver.find_element(By.ID,"checkout").click() # buka keranjang
        driver.find_element(By.ID, "first-name").send_keys("standard") # isi nama depan
        driver.find_element(By.ID, "last-name").send_keys("user") # isi nama belakang
        driver.find_element(By.ID, "postal-code").send_keys("1234") # isi nama belakang
        driver.find_element(By.ID,"continue").click() # lanjutkan 
        driver.find_element(By.ID,"finish").click() # selesaikan checkout


    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()