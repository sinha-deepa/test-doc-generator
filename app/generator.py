import os
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError, AuthenticationError
from app.prompt_builder import build_prompt


# -------------------------
# Load environment variables
# -------------------------
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)


# -------------------------
# Utility function to read files
# -------------------------
def read_file(path):
    with open(path, "r") as f:
        return f.read()


# -------------------------
# Read inputs
# -------------------------
jira = read_file("input_samples/sample_jira.txt")
ui = read_file("input_samples/sample_ui_details.txt")
db = read_file("input_samples/sample_db_schema.txt")

test_plan_template = read_file("templates/test_plan_template.txt")
test_case_template = read_file("templates/test_case_template.txt")


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
# Call LLM with safe handling
# -------------------------
try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    output = response.choices[0].message.content

except RateLimitError:
    output = """
ERROR: API QUOTA EXCEEDED

Your code and prompt are correct.
Your OpenAI account currently has no usable quota.

👉 Temporary workaround:
- Use the SAME prompt in:
  • ChatGPT UI
  • GitHub Copilot Chat (inside IntelliJ)

👉 Permanent fix:
- Enable billing on OpenAI account (even $5 is enough)
"""

except AuthenticationError:
    output = """
ERROR: AUTHENTICATION FAILED

Please check:
- OPENAI_API_KEY value in .env file
- No extra spaces or quotes
"""

except Exception as e:
    output = f"""
UNEXPECTED ERROR OCCURRED:
{str(e)}
"""


# -------------------------
# Save output
# -------------------------
os.makedirs("output", exist_ok=True)

with open("output/generated_test_doc.txt", "w") as f:
    f.write(output)


# -------------------------
# Console feedback
# -------------------------
print("\n==============================")
print(" TEST DOCUMENT GENERATION DONE ")
print("==============================\n")
print(output)
