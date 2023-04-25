from selenium.webdriver.common.by import By


class AddItem:
    products_page_url = 'https://www.saucedemo.com/inventory.html'
    item_selector = (By.CSS_SELECTOR, 'div.page_wrapper div.inventory_container div.inventory_list div.inventory_item:nth-child(1) div.inventory_item_description div.inventory_item_label a:nth-child(1) > div.inventory_item_name')
    add_button_selector = (By.ID, 'add-to-cart-sauce-labs-backpack')
    back_to_products_selector = (By.ID, 'back-to-products')

    def __init__(self, browser):
        self.driver = browser.driver

    def get_product_page(self):
        self.driver.get(self.products_page_url)

    def click_item(self):
        additem = self.driver.find_element(*self.item_selector)
        additem.click()

    def click_add_button(self):
        add_button = self.driver.find_element(*self.add_button_selector)
        add_button.click()

    def go_back_products(self):
        go_back = self.driver.find_element(*self.back_to_products_selector)
        go_back.click()
