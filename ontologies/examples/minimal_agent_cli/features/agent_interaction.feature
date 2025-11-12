Feature: Agent Basic Interaction
  As a user
  I want to interact with the agent
  So that I can verify its core reasoning capabilities

  Scenario: Agent responds based on its purpose
    Given the agent is running
    When the user asks "What is your purpose?"
    Then the agent's response should contain "provide a tangible starting point for developers"
