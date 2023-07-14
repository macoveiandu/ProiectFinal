from behave import *

@Given('I am in login page')
def step_impl(context):
    context.login_page.get_page()

@When('I input a username and pass')
def step_impl(context):
    context.login_page.input_username('problem_user')
    context.login_page.input_password('secret_sauce')
    #sleep(1)

@When ('I click on login button')
def step_impl(context):
    context.login_page.click_login_button()

@Then('I am on main page')
def step_impl(context):
    #sleep(3)
    assert context.login_page.get_url() == 'https://www.saucedemo.com/inventory.html'

#-------------

@Given ('I am on the prod page')
def step_impl(context):
    assert context.login_page.get_url() == 'https://www.saucedemo.com/inventory.html'
@When ('Click to add all to inventory')
def step_impl(context):
    context.add_item.click_add_item()
    context.add_item.go_to_inv()
@Then ('I check its all in inventory')
def step_impl(context):
    context.inventory.inventory_count()

#--------------
@Given ('I am on the products page')
def step_impl(context):
    assert context.login_page.get_url() == 'https://www.saucedemo.com/inventory.html'
@When ('Add all items to inventory')
def step_impl(context):
    context.context.add_item.click_add_item()
@Then ('I click on inventory to remove all items and check it')
def step_impl(context):
    context.remove_item.click_item_remove()
    context.remove_item.check_items_removed()
