Feature: problem_user add and remove all items
  Background:
    Given I am in login page
    When I input a username and pass
    And  I click on login button
    Then I am on main page

  @adaugareProdusInCos
  Scenario: Add all items to inventory
    Given I am on the products page
    When Click to add all to inventory
    Then I check its all in inventory

  @stergereProduseDinCos
  Scenario: Remove all items from inventory
    Given I am on the products page
    When Add all items to inventory
    Then I click on inventory to remove all items and check it
