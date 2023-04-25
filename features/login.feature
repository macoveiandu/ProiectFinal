Feature: Login on app

  @logare
  Scenario: Login success
    Given I am on the login page
    When I input a username a password and click on login button
    Then I am on the main page
