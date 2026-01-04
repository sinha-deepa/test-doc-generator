def build_prompt(jira, ui, db, test_plan_template, test_case_template):
    return f"""
You are a Senior QA Engineer with expertise in manual, API, and DB testing.

Your task is to generate a COMPLETE Test Plan and Test Cases with full coverage.

JIRA DESCRIPTION:
{jira}

UI / DESIGN DETAILS:
{ui}

DATABASE DETAILS:
{db}

TEST PLAN TEMPLATE:
{test_plan_template}

TEST CASE TEMPLATE:
{test_case_template}

Instructions:
- Cover functional, negative, edge, API, and DB scenarios
- Infer missing but obvious cases
- Follow templates strictly
- Avoid duplicate test cases

Output only Test Plan and Test Cases.
"""
