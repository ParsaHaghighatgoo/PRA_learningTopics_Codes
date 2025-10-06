Feature: Email summarization by AI agent

  Background:
    Given the AI agent is logged into Gmail
    And connected to the email inbox

  Scenario: Summarize a new email and store the summary
    Given a new unread email arrives in the inbox
    When the AI agent detects the new email
    Then the AI agent reads the email content
    And the AI agent generates a summary of the email
    And stores the summary into a text file