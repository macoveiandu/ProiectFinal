Feature: add item to inventory
  Background:
    Given I am on the login page
    When I input a username "standard_user" and password "secret_sauce"
    And  I click on login button
    Then I am on the main page

  @adaugareprodusincos
  Scenario: Add item to inventory
    Given I am on the items page
    When Click to add to inventory
    Then I click on inventory

  @finalizareComanda
  Scenario: Finish order
    Given I am on the product page and click Checkout
    When I fill with data
    And I click Continue to finish order
    Then Apear Order Complete