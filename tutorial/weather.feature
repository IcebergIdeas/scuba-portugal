Feature: Show weather


  Scenario: Show the weather for today
    Given I am on the login page
    When I press the weather button
    Then the weather for Lisbon is displayed