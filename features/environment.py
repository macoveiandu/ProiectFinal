from features.browser import Browser
from pages.add_item import AddItem
from pages.iamge import Image
from pages.inventory import Inventory
from pages.login_page import LoginPage
from pages.remove_item import RemoveItem


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage(context.browser)
    context.add_item = AddItem(context.browser)
    context.remove_item = RemoveItem(context.browser)
    context.inventory = Inventory(context.browser)
    context.image = Image(context.browser)


def after_all(context):
    context.browser.quit()
