from behave import *
from time import sleep


@Given('I am on the products page')
def step_impl(context):
    context.add_item.get_product_page()
    context.add_item.click_item()


@When('Click to add to inventory')
def step_impl(context):
    context.add_item.click_add_button()


@Then('I continue shopping')
def step_impl(context):
    context.add_item.go_back_products()
