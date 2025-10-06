Feature: AI agent replies to new emails with a summary

  Scenario: New email received
    Given a new email is received in the inbox
    When the AI agent detects the new email
    Then the AI agent generates a predefined summary of the email
    And the AI agent sends the summary as a reply to the sender
