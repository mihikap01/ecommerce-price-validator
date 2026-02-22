Feature: Ebay Regression

  Background: Generic navigation
    Given Navigate to the target website

  Scenario: All gift items are under $25
    Then Click on gifts under 25
    Then Check if all gifts are under 25
