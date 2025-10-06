# features/steps/summarize_emails_steps.py
from behave import given, when, then
from pathlib import Path
from datetime import datetime

# -------------------------------
# Helpers (you can replace later)
# -------------------------------

class FakeInbox:
    """
    A tiny in-memory inbox so your feature can run without real Gmail.
    Swap this with a Gmail client later.
    """
    def __init__(self):
        self.connected = False
        self.unread = []

    def connect(self):
        self.connected = True

    def add_unread(self, subject, sender, body):
        self.unread.append({"subject": subject, "from": sender, "body": body})

    def get_latest_unread(self):
        return self.unread[0] if self.unread else None

    def mark_as_read(self, email):
        if email in self.unread:
            self.unread.remove(email)

def summarize_text(text: str, max_words: int = 40) -> str:
    """
    Super-simple "summary":
    - Take first sentence up to punctuation, else first N words.
    - Trim to max_words.
    Replace this with an LLM call later.
    """
    if not text:
        return ""
    # naive first-sentence split
    for sep in [".", "!", "?"]:
        if sep in text:
            first_sentence = text.split(sep)[0].strip()
            break
    else:
        first_sentence = text.strip()

    words = first_sentence.split()
    if len(words) > max_words:
        return " ".join(words[:max_words]) + " ..."
    return first_sentence

def store_summary(summary: str, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().isoformat(timespec="seconds")
    with out_path.open("a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {summary}\n")

# -------------------------------
# Background
# -------------------------------

@given("the AI agent is logged into Gmail")
def step_logged_into_gmail(context):
    # In the fake mode, "login" is a no-op.
    # Later, initialize your real Gmail client and store it on context.
    context.inbox = FakeInbox()
    context.logged_in = True
    assert context.logged_in is True

@given("connected to the email inbox")
def step_connected_to_inbox(context):
    # Fake connect
    context.inbox.connect()
    assert context.inbox.connected is True

# -------------------------------
# Scenario steps
# -------------------------------

@given("a new unread email arrives in the inbox")
def step_new_unread_email(context):
    # Seed a fake unread email for the test
    context.inbox.add_unread(
        subject="Welcome to the team",
        sender="founder@startup.example",
        body=(
            "Hey there! Excited to have you onboard. "
            "Here are three things to do this week: "
            "1) set up your dev environment, "
            "2) read the RPA design doc, "
            "3) ship a tiny agent. Let's go! 🎉"
        ),
    )

@when("the AI agent detects the new email")
def step_detect_new_email(context):
    email = context.inbox.get_latest_unread()
    context.latest_email = email
    assert context.latest_email is not None

@then("the AI agent reads the email content")
def step_read_email(context):
    email = context.latest_email
    assert isinstance(email, dict) and "body" in email and email["body"]

@then("the AI agent generates a summary of the email")
def step_generate_summary(context):
    email = context.latest_email
    context.summary = summarize_text(email["body"], max_words=40)
    assert context.summary and isinstance(context.summary, str)

@then("stores the summary into a text file")
def step_store_summary(context):
    # Choose where to store summaries; you can change this path.
    out_path = Path("artifacts/email_summaries.txt")
    store_summary(context.summary, out_path)
    context.summary_file = out_path
    assert out_path.exists() and out_path.stat().st_size > 0
    # Mark as read (fake)
    context.inbox.mark_as_read(context.latest_email)
