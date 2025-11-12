# Minimal Runnable CLI Agent

This example provides a minimal, hands-on, and **runnable** Python prototype that demonstrates the core feedback loop of a governed autonomous agent. It connects static ontology definitions (Agent Profile, Delegation) with a dynamic Large Language Model (LLM) to create a simple, command-line-driven intelligent agent.

## Purpose

The goal of this example is to provide a tangible starting point for developers. It showcases the "last mile" of how the Agent Ontology comes to life when paired with an LLM, moving from theoretical models to a working implementation. You can use this as a foundation to build your own more complex agents.

## Environment Setup

You can set up the environment using either a standard Python virtual environment or a reproducible Nix shell.

### Option 1: Using Python `venv` (Standard Method)

1.  **Create a virtual environment:**
    ```bash
    python3 -m venv .venv
    ```

2.  **Activate the environment:**
    ```bash
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Option 2: Using Nix (Reproducible Environment)

If you have [Nix](https://nixos.org/download.html) installed, you can get a completely reproducible environment.

1.  **Enter the Nix shell:**
    From this directory (`ontologies/examples/minimal_agent_cli/`), run:
    ```bash
    nix-shell
    ```
    This command will automatically download all specified dependencies, including the correct Python version, and configure the shell. You will see a prompt like `(agent-env):...$` when it's active.

## Configuration

The agent requires an OpenAI API key to function.

1.  **Create a `.env` file:**
    Copy the example environment file:
    ```bash
    cp .env.example .env
    ```

2.  **Add your API key:**
    Open the `.env` file and replace `your-openai-api-key-here` with your actual OpenAI API key.

## How to Run the Agent

Once your environment is set up and configured:

1.  **Run the script:**
    ```bash
    python run_agent.py
    ```

2.  **Interact with the agent:**
    The script will load the agent's profile and delegation rules from the JSON-LD files. It will then prompt you for a command. You can type in a natural language instruction, for example:
    ```
    > What is the primary goal of this project?
    ```
    The agent will use the LLM to interpret your intent within the context of its defined purpose and respond.

## Behavior-Driven Development (BDD) Tests

This example includes a simple BDD test to verify the agent's behavior using `behave`.

### 1. BDD Feature File

Here is a sample feature file that describes how the agent should behave.

**File: `features/agent_interaction.feature`**
```gherkin
Feature: Agent Basic Interaction
  As a user
  I want to interact with the agent
  So that I can verify its core reasoning capabilities

  Scenario: Agent responds based on its purpose
    Given the agent is running
    When the user asks "What is your purpose?"
    Then the agent's response should contain "provide a tangible starting point for developers"
```

### 2. Running the Tests

To run the BDD tests, you first need to install `behave`:

```bash
pip install behave
```
*(Note: If you are using the Nix environment, `behave` is already included.)*

Then, execute the tests from this directory:
```bash
behave
```

The test runner will find the `features/` directory, execute the scenarios, and report whether the agent's behavior matches the expectations defined in the `.feature` files.

### LLM Recommendation

- At least above 120b.
