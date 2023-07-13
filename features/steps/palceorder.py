from behave import *
@Given('I am on the login page')
def step_impl(context):
    context.login_page.get_page()

@When('I input a username "problem_user" and password "secret_sauce"')
def step_impl(context,user,pwd):
    context.login_page.input_username(user)
    context.login_page.input_password(pwd)
    #sleep(1)

@When ('I click on login button')
def step_impl(context):
    context.login_page.click_login_button()

@Then('I am on the main page')
def step_impl(context):
    #sleep(3)
    assert context.login_page.get_url() == 'https://www.saucedemo.com/inventory.html'



@Given ('I am on the products page')
@When ('Click to add all to inventory')
@Then ('I click to remove all items')


@Given ('I add all products in inventory')
@When ('I am on the inventory page and click Checkout')
@When ('I enter all data for order')
@Then ('I click Continue to Finish order')
