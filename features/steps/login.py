from time import sleep
from behave import *

@Given('I am on the login page')
def step_impl(context):
    context.login_page.get_page()

@When('I input a username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.login_page.input_username(user)
    context.login_page.input_password(pwd)
    #sleep(1)

@When ('I click on login buton')
def step_impl(context):
    context.login_page.click_login_button()

@Then('I am on the main page')
def step_impl(context):
    #sleep(3)
    assert context.login_page.get_url() == 'https://www.saucedemo.com/inventory.html'



