Feature: Login on app

  @logare
  Scenario: Login success
    Given I am on the login page
    When I input a username "standard_user" and password "secret_sauce"
    And  I click on login button
    Then I am on the main page

  Scenario Outline: Login with multiple parametres
    Given I am on the login page
    When I input a username "<username>" and password "<password>"
    And  I click on login buton
    Then I am on the main page

    Examples:
    |        username            |   password   |
    |   standard_user            | secret_sauce |
    |   locked_out_user          | secret_sauce |
    |   problem_user             | secret_sauce |
    |   performance_glitch_user  | secret_sauce |