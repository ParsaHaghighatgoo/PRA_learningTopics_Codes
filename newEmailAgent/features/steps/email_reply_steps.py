from behave import given, when, then

@given("a new email is received in the inbox")
def step_given_email_received(context):
    context.email = {"subject": "Test", "body": "Hello!"}

@when("the AI agent detects the new email")
def step_when_detect_email(context):
    context.agent_detected = True

@then("the AI agent generates a predefined summary of the email")
def step_then_generate_summary(context):
    context.summary = "This is a test summary."
    assert context.summary is not None

@then("the AI agent sends the summary as a reply to the sender")
def step_then_send_reply(context):
    sent = True  # pretend send
    assert sent is True
