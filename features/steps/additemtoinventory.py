from behave import *
from time import sleep


@Given('I am on the items page')
def step_impl(context):
    context.add_item.get_product_page()
    sleep(1)

@When('Click to add to inventory')
def step_impl(context):
    context.add_item.click_add_item()

@Then('I click on inventory')
def step_impl(context):
    context.add_item.go_to_inv()

@Given ('I am on the product page and click Checkout')
def step_impl(context):
    #context.add_item.get_product_page()
    #context.add_item.click_add_item()
    context.add_item.go_to_inv()
    context.inventory.click_chekout()

@When ('I fill with data')
def step_impl(context):
    context.inventory.insert_data()

@When ('I click Continue to finish order')
def step_impl(context):
    context.inventory.finis_order()

@Then('Apear Order Complete')
def step_impl(context):
    context.inventory.complete_check()