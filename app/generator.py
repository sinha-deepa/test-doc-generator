import os
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError, AuthenticationError
from app.prompt_builder import build_prompt

# -------------------------
# Load environment variables
# -------------------------
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# -------------------------
# Utility functions
# -------------------------
def read_file_optional(path, default_text):
    if os.path.exists(path):
        with open(path, "r") as f:
            content = f.read().strip()
            return content if content else default_text
    return default_text


def read_file_mandatory(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Mandatory input missing: {path}")
    with open(path, "r") as f:
        content = f.read().strip()
        if not content:
            raise ValueError(f"Mandatory input is empty: {path}")
        return content


# -------------------------
# Read inputs
# -------------------------
try:
    # MANDATORY
    jira = read_file_mandatory("input/jira_description.txt")

    # OPTIONAL
    ui = read_file_optional(
        "input/ui_details.txt",
        "UI details not provided. Infer UI scenarios based on Jira description."
    )

    db = read_file_optional(
        "input/db_schema.txt",
        "Database details not provided. Infer DB validation scenarios."
    )

    test_plan_template = read_file_optional(
        "templates/test_plan_template.txt",
        "Generate a standard QA Test Plan using industry best practices."
    )

    test_case_template = read_file_optional(
        "templates/test_case_template.txt",
        "Generate detailed test cases with steps, data, and expected results."
    )

except (FileNotFoundError, ValueError) as e:
    print("\n❌ INPUT ERROR")
    print(str(e))
    exit(1)


# -------------------------
# Build prompt
# -------------------------
prompt = build_prompt(
    jira,
    ui,
    db,
    test_plan_template,
    test_case_template
)


# -------------------------
# Call LLM safely
# -------------------------
try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    output = response.choices[0].message.content

except RateLimitError:
    output = """
ERROR: API quota exceeded.

Use the SAME prompt in:
- GitHub Copilot Chat
- ChatGPT UI

Jira input is mandatory; others are optional.
"""

except AuthenticationError:
    output = "ERROR: Invalid OpenAI API key."

except Exception as e:
    output = f"Unexpected error occurred: {str(e)}"


# -------------------------
# Save output
# -------------------------
os.makedirs("output", exist_ok=True)

with open("output/generated_test_doc.md", "w") as f:
    f.write(output)


# -------------------------
# Final message
# -------------------------
print("\n✅ Test Document Generation Completed")
print("📄 Output saved at: output/generated_test_doc.md")
