📄 TestDocGenerator – AI-Based Test Plan & Test Case Generator

This project helps generate complete Test Plans and Test Cases with full coverage using:

Jira descriptions (plain English)

UI / design details

Database schema details

Fixed Test Plan & Test Case templates

The project supports TWO execution modes:

Python (API-based execution)

Copilot-first (No API / No Code execution)

📁 Project Structure
TestDocGenerator/
│
├── app/                     # Python execution (API mode)
│   ├── generator.py
│   └── prompt_builder.py
│
├── prompts/                 # Copilot-first execution
│   └── test_doc_prompt.md
│
├── input/                   # User inputs
│   ├── jira_description.txt
│   ├── ui_details.txt
│   └── db_schema.txt
│
├── templates/               # Fixed QA templates
│   ├── test_plan_template.txt
│   └── test_case_template.txt
│
├── output/                  # Generated output
│   └── generated_test_doc.md
│
├── .env
├── requirements.txt
└── README.md

🚀 RUN FLOW 1: Run via Python (API Mode)

✅ Use this when OpenAI API billing & quota are available.

🔧 Prerequisites

Python 3.9+

Virtual environment activated

Valid OpenAI API key with billing enabled

🔹 Step 1: Install dependencies

From project root:

pip install -r requirements.txt

🔹 Step 2: Set API key

Edit .env file:

OPENAI_API_KEY=sk-xxxxxx


⚠️ Do not commit this file to GitHub.

🔹 Step 3: Update input files

Edit:

input/jira_description.txt

input/ui_details.txt

input/db_schema.txt

🔹 Step 4: Run the application

From project root:

python -m app.generator

🔹 Step 5: View output

Generated Test Plan & Test Cases will be saved to:

output/generated_test_doc.md

⚠️ Common Issues (API Mode)

401 Error → Invalid API key

429 Error → Quota / billing not enabled

👉 If API issues occur, use Run Flow 2 (Copilot-first).

🤖 RUN FLOW 2: Run via Copilot Prompt (NO API, Recommended)

✅ Works without OpenAI API
✅ Best for learning, demos, and non-tech users
✅ Uses GitHub Copilot Chat inside IntelliJ

🔹 Step 1: Fill input files

Update these files in plain English:

input/jira_description.txt

input/ui_details.txt

input/db_schema.txt

🔹 Step 2: Open master prompt

Open:

prompts/test_doc_prompt.md

🔹 Step 3: Replace placeholders

Inside test_doc_prompt.md:

Copy content from input files

Paste into respective sections

Copy templates from templates/ folder

Ensure no <PASTE CONTENT> placeholders remain

Save the file.

🔹 Step 4: Execute using Copilot Chat

Select ALL content in test_doc_prompt.md

Copy (Cmd + A, Cmd + C)

Open Copilot Chat in IntelliJ

Mac: Cmd + Shift + I

Windows: Ctrl + Shift + I

Paste content

Press Enter

➡️ This is the RUN action.

🔹 Step 5: Save output

Copy Copilot’s response

Paste into:

output/generated_test_doc.md


Save.


