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

  @stergereProduseDinCos
  Scenario: Remove all items from inventory
    Given I am on the products page
    When Click to add all to inventory
    Then I click on inventory to remove all items

  @verificarepozeproduse
  Scenario: Check products images
    Given I am on the product page i check image
    When I click on product
    Then check images are the same

  @verificarelinkproduse
  Scenario: Check products link working
    Given I am on the products page
    When I click on product
    Then products its correct