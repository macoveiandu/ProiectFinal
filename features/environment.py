from features.browser import Browser
from features.pages.add_item import AddItem
from features.pages.login_page import LoginPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage(context.browser)
    context.add_item = AddItem(context.browser)


def after_all(context):
    context.browser.quit()
