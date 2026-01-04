You are a Senior QA Engineer with strong experience in
manual testing, API testing, database validation, and test strategy.

Your task is to generate a COMPLETE Test Plan and Test Cases
with full coverage for the given feature.

Inputs provided:
1. Jira description (plain English)
2. UI / design details
3. Database schema details
4. Fixed Test Plan template
5. Fixed Test Case template

Responsibilities:
- Understand functional requirements
- Infer missing but obvious scenarios
- Cover positive, negative, edge, and boundary cases
- Include UI, API, and DB validation where applicable
- Follow templates strictly
- Avoid duplicate test cases
- Use clear, professional QA language

====================
JIRA DESCRIPTION
====================
Feature: User Profile Update

Users should be able to update name, email, and phone number.
Validations should be applied on email and phone fields.


====================
UI / DESIGN DETAILS
====================
Profile screen contains:
- Name input field
- Email input field
- Phone number field
- Save button
- Success and error messages


====================
DATABASE DETAILS
====================
Table: users
Columns:
- id (PK)
- name
- email
- phone
- updated_at


====================
TEST PLAN TEMPLATE
====================
TEST PLAN

1. Objective
   Define the purpose of testing.

2. Scope
   In Scope:
   Out of Scope:

3. Test Approach
   Manual, API, DB validation.

4. Test Types
   Functional, Negative, Edge, Regression, API, DB.

5. Test Environment
   OS, Browser/App, Build version.

6. Test Data Strategy
   Valid, invalid, boundary data.

7. Entry Criteria
   Build available, test data ready.

8. Exit Criteria
   All critical test cases executed.

9. Risks & Mitigation
   Dependencies, environment issues.

10. Assumptions
    APIs and DB are accessible.


====================
TEST CASE TEMPLATE
====================
TEST CASE TEMPLATE

Test Case ID:
Title:
Description:

Preconditions:

Test Steps:
1.
2.
3.

Test Data:

Expected Result:

Priority:
High / Medium / Low

Type:
Functional / Negative / Edge / API / DB

====================
OUTPUT FORMAT
====================
1. Test Plan (filled using template)
2. Test Cases (detailed, structured)
   Do not add explanations.
