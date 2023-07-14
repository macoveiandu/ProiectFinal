Feature: problem_user add and remove all items
  Background:
    Given I am on the login page
    When I input a username and password
    And  I click login button
    Then I am on the first page

  @adaugareProdusInCos
  Scenario: Add all items to inventory
    Given I am on the prod page
    When Click to add all items to inventory
    Then I go to inventory

  @ComandareProduse
  Scenario: comandare produse
     Given I add all products in inventory
     When I am on the inventory page and click Checkout
     And I enter all data for order
     Then I click Continue to Finish order

