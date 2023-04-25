Feature: add item to inventory
  Background:
    Given I am on the login page
    When I input a username a password and click on login button
    Then I am on the main page

  @adaugareprodusincos
  Scenario: Add item to inventory
    Given I am on the products page
    When Click to add to inventory
    Then I continue shopping