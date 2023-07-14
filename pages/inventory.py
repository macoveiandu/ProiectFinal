from selenium.webdriver.common.by import By
from time import sleep
class Inventory:
    inventory_page = 'https://www.saucedemo.com/cart.html'
    Check_button = (By.ID, 'checkout')
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')
    COMPLETE_ORDER = (By.CLASS_NAME, 'complete-header')
    INV_COUNT = (By.CLASS_NAME, 'shopping_cart_badge')

    def __init__(self, browser):
        self.driver = browser.driver

    def click_chekout(self):
        sleep(1)
        self.driver.execute_script(("window.scrollTo(0, document.body.scrollHeight);"))
        self.driver.find_element(*self.Check_button).click()


    def insert_data(self):
        sleep(1)
        firstname = self.driver.find_element(*self.FIRST_NAME)
        firstname.send_keys('Macovei')
        lastname = self.driver.find_element(*self.LAST_NAME)
        lastname.send_keys('Andrei')
        postalcode = self.driver.find_element(*self.POSTAL_CODE)
        postalcode.send_keys('720266')

    def finis_order(self):
        sleep(1)
        finish = self.driver.find_element(*self.CONTINUE_BUTTON)
        finish.click()
        finisbutton = self.driver.find_element(*self.FINISH_BUTTON)
        finisbutton.click()

    def inventory_count(self):
        inv_qnt = self.driver.find_element(*self.INV_COUNT).text
        return inv_qnt == 6

    def complete_check(self):
        complete = self.driver.find_element(*self.COMPLETE_ORDER).text
        if complete == 'Thank you for your order!':
            return complete
