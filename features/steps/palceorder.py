from behave import *
@Given('I am on the login pag')
def step_impl(context):
    context.login_page.get_page()

@When('I input a username and password')
def step_impl(context):
    context.login_page.input_username('problem_user')
    context.login_page.input_password('secret_sauce')
    #sleep(1)

@When ('I click login button')
def step_impl(context):
    context.login_page.click_login_button()

@Then('I am on the first page')
def step_impl(context):
    #sleep(3)
    assert context.login_page.get_url() == 'https://www.saucedemo.com/inventory.html'


#---------------------------
@Given ('I am on the product page')
def step_impl(context):
    assert context.login_page.get_url() == 'https://www.saucedemo.com/inventory.html'
@When ('Click to add all items to inventory')
def step_impl(context):
    context.add_item.go_to_inv()
@Then('I go to inventory')
def step_impl(context):
    context.add_item.go_to_inv()
#---------------------------

@Given ('I add all products in inventory')
def step_impl(context):
    context.add_item.click_add_item()
@When ('I am on the inventory page and click Checkout')
def step_impl(context):
    assert context.login_page.get_url() == 'https://www.saucedemo.com/inventory.html'
    context.add_item.go_to_inv()
    context.inventory.click_chekout()
@When ('I enter all data for order')
def step_impl(context):
    context.inventory.insert_data()
@Then ('I click Continue to Finish order')
def step_impl(context):
    context.inventory.finis_order()