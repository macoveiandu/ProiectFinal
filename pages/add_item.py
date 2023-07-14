from selenium.webdriver.common.by import By
from time import sleep


class AddItem:
    products_page_url = 'https://www.saucedemo.com/inventory.html'
    add_button_selector1 = (By.ID, 'add-to-cart-sauce-labs-backpack')
    add_button_selector2 = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    add_button_selector3 = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    add_button_selector4 = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    add_button_selector5 = (By.ID, 'add-to-cart-sauce-labs-onesie')
    add_button_selector6 = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
    go_to_inventory = (By.XPATH,'//*[@id="shopping_cart_container"]/a')

    def __init__(self, browser):
        self.driver = browser.driver

    def get_product_page(self):
        self.driver.get(self.products_page_url)

    def click_add_item(self):
        self.driver.find_element(*self.add_button_selector1).click()
        self.driver.find_element(*self.add_button_selector2).click()
        self.driver.find_element(*self.add_button_selector3).click()
        self.driver.find_element(*self.add_button_selector4).click()
        self.driver.find_element(*self.add_button_selector5).click()
        self.driver.find_element(*self.add_button_selector6).click()

    def go_to_inv(self):
        self.driver.find_element(*self.go_to_inventory).click()
        sleep(1)
