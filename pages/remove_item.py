from selenium.webdriver.common.by import By


class RemoveItem:
    products_page_url = 'https://www.saucedemo.com/inventory.html'
    item_button_remove1 = (By.ID,'remove-sauce-labs-backpack')
    item_button_remove2 = (By.ID, 'remove-sauce-labs-bike-light')
    item_button_remove3 = (By.ID, 'remove-sauce-labs-bolt-t-shirt')
    item_button_remove4 = (By.ID, 'remove-sauce-labs-fleece-jacket')
    item_button_remove5 = (By.ID, 'remove-sauce-labs-onesie')
    item_button_remove6 = (By.ID, 'remove-test.allthethings()-t-shirt-(red)')
    inventory_count = (By.CLASS_NAME,'shopping_cart_badge')
    lista = [item_button_remove1,item_button_remove2,item_button_remove3,item_button_remove4,item_button_remove5,item_button_remove6]

    def __init__(self, browser):
        self.driver = browser.driver

    def get_product_page(self):
        self.driver.get(self.products_page_url)

    def click_item_remove(self):
        self.driver.find_element(*self.item_button_remove1).click()
        self.driver.find_element(*self.item_button__remove2).click()
        self.driver.find_element(*self.item_button__remove3).click()
        self.driver.find_element(*self.item_button__remove4).click()
        self.driver.find_element(*self.item_button__remove5).click()
        self.driver.find_element(*self.item_button__remove6).click()

    def check_items_removed(self):
        try:
            check_inv = self.driver.find_element(*self.inventory_count).text
        except:
            assert False, 'Test picat'
        if check_inv == 0:
            assert True, 'Test trecut'
