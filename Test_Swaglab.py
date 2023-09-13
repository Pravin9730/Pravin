import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# username = "admin"
# password = "admin"
class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_alogin(self):
        driver = self.driver
        driver.get("http://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        username_element = driver.find_element(By.ID,"user-name")
        username_element.send_keys("standard_user")
        time.sleep(2)
        password_element = driver.find_element(By.ID,"password")
        password_element.send_keys("secret_sauce")
        time.sleep(2)
        # password_element.send_keys(Keys.RETURN)
        loginele = driver.find_element(By.XPATH, "//input[@id='login-button']")
        loginele.click()
        time.sleep(2)
        assert "Logged In"

    def test_btitle(self):
        driver = self.driver
        driver.get("http://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        username_element = driver.find_element(By.ID,"user-name")
        username_element.send_keys("standard_user")
        time.sleep(2)
        password_element = driver.find_element(By.ID,"password")
        password_element.send_keys("secret_sauce")
        time.sleep(2)
        # password_element.send_keys(Keys.RETURN)
        loginele = driver.find_element(By.XPATH, "//input[@id='login-button']")
        loginele.click()
        time.sleep(2)
        if self.driver.title == "Swag Labs":
            print('Title verified')
        else:
            print('Wrong Title')

    def test_cCart(self):
        driver = self.driver
        driver.get("http://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        username_element = driver.find_element(By.ID,"user-name")
        username_element.send_keys("standard_user")
        time.sleep(2)
        password_element = driver.find_element(By.ID,"password")
        password_element.send_keys("secret_sauce")
        loginele = driver.find_element(By.XPATH, "//input[@id='login-button']")
        loginele.click()
        time.sleep(2)
        # password_element.send_keys(Keys.RETURN)
        add_to_Cart = driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
        add_to_Cart.click()
        time.sleep(2)


    def test_dremovecart(self):
        driver = self.driver
        driver.get("http://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        username_element = driver.find_element(By.ID,"user-name")
        username_element.send_keys("standard_user")
        time.sleep(2)
        password_element = driver.find_element(By.ID,"password")
        password_element.send_keys("secret_sauce")
        loginele = driver.find_element(By.XPATH, "//input[@id='login-button']")
        loginele.click()
        time.sleep(1)
        add_to_Cart = driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
        add_to_Cart.click()
        time.sleep(1)
        # password_element.send_keys(Keys.RETURN)
        check_cart = driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']")
        check_cart.click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, "//*[text()='Sauce Labs Backpack']").is_displayed()
        remove_btn = driver.find_element(By.XPATH,"//button[@id='remove-sauce-labs-backpack']")
        remove_btn.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
