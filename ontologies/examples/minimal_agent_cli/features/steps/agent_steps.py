from behave import given, when, then
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# --- Initialization ---
load_dotenv()

# --- LLM Client Setup ---
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:1234/v1")
client = OpenAI(base_url=LLM_BASE_URL, api_key=os.getenv("OPENAI_API_KEY", "sk-not-needed-for-local"))

# --- Load Agent's "Identity" and "Authorization" ---
try:
    with open("agent_profile.jsonld", "r") as f:
        AGENT_PROFILE = json.load(f)
    with open("delegation.jsonld", "r") as f:
        DELEGATION = json.load(f)
except FileNotFoundError as e:
    print(f"Error: Could not find config file {e.filename}.")
    exit()

def ask_llm_for_purpose(user_prompt):
    """A simplified function to ask the LLM about its purpose based on the agent profile."""
    system_prompt = f"""
    You are an AI assistant defined by the following Agent Profile.
    Your task is to answer questions about your purpose and capabilities based *only* on this profile.
    Do not invent new information.

    Agent Profile:
    {json.dumps(AGENT_PROFILE)}
    """
    try:
        model_name = "local-model"
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.1
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred while interacting with the LLM: {e}")
        return None

@given('the agent is running')
def step_given_agent_running(context):
    context.agent_is_running = True

@when('the user asks "{question}"')
def step_when_user_asks(context, question):
    assert context.agent_is_running
    context.response = ask_llm_for_purpose(question)
    assert context.response is not None, "Failed to get a response from the LLM."

@then('the agent\'s response should contain "{expected_text}"')
def step_then_response_contains(context, expected_text):
    assert expected_text.lower() in context.response.lower(), f"Expected response to contain '{expected_text}', but got '{context.response}'"
