from time import sleep

from behave import *


@Given('I am on the login page')
def step_impl(context):
    context.login_page.get_page()


@When('I input a username a password and click on login button')
def step_impl(context):
    context.login_page.input_username('standard_user')
    context.login_page.input_password('secret_sauce')
    context.login_page.click_login_button()


@Then('I am on the main page')
def step_impl(context):
    #sleep(3)
    assert context.login_page.get_url() == 'https://www.saucedemo.com/inventory.html'
