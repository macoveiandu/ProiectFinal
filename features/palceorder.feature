Feature: problem_user add and remove all items
  Background:
    Given I am on the login page
    When I input a username "problem_user" and password "secret_sauce"
    And  I click on login button
    Then I am on the main page

  @adaugareProdusInCos
  Scenario: Add all items to inventory
    Given I am on the products page
    When Click to add all to inventory
    Then I click to remove all items

   @ComandareProduse
     Scenario: comandare produse
     Given I add all products in inventory
     When I am on the inventory page and click Checkout
     And I enter all data for order
     Then I click Continue to Finish order

