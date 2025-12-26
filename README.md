## Vault of Codes – Personal Expense Tracker using Python
----
## Project Description
description: >
This project implements a Personal Expense Tracker using Python as part of
the Vault of Codes Internship (Assignment A3). The application allows users
to record daily expenses, manage monthly income, and analyze total spending
through a menu-driven command-line interface. Expense data is stored
permanently using JSON file handling, enabling users to track their
financial activities across multiple sessions.

---

## Objective
objective: >
To develop a simple and efficient personal finance management system that
helps users track expenses, calculate total spending, manage monthly income,
and determine remaining balance using core Python programming concepts.

---

## Features
features:
Add daily expenses with amount, category, and date

Store expense data using JSON file handling

Automatically calculate total expenses

Add and edit monthly income (supports variable income users)

Calculate remaining balance (savings)

View category-wise expense summary

Display overspending warning messages

Menu-driven command-line interface

---

## Tech Stack
tech_stack:


Python

JSON (File Handling)

Command-Line Interface (CLI)

Visual Studio Code

---

## Data Storage
data_storage:
file_format: "JSON"

file_name: "expenses.json"

description: >
Expense records are stored as a list of dictionaries in JSON format.
Each record contains details such as expense amount, category, and date.
This ensures data persistence even after the application is closed.

---

## How to Run
how_to_run:
requirements: "Python 3.x"

steps:

- Clone the repository or download the project files
- Navigate to the project directory
- Run the application using the command below
- 
run_command: "python expense_tracker.py"

---

## Sample Output
sample_output: >

Enter monthly income: 30000

Monthly income saved successfully.

--- Personal Expense Tracker ---

Add Expense

View All Expenses

Edit Expense

Delete Expense

View Financial Summary

Category-wise Summary

Edit Monthly Income

Exit

Enter expense amount: 2000

Enter category: Food

Expense added successfully.

Enter expense amount: 1000

Enter category: Transport

Expense added successfully.

--- Financial Summary ---

Monthly Income : 30000

Total Spent : 3000

Remaining : 27000

---

## Project Structure
project_structure>

expense_tracker.py

expenses.json

README.md

---

## Learning Outcomes
learning_outcomes:
Hands-on experience with Python programming

Practical understanding of file handling using JSON

Improved knowledge of data structures and control flow

Experience in building a real-world finance tracking application

Enhanced logical thinking and problem-solving skills

---

## Internship Details
internship_details: >
This project was developed as part of the Vault of Codes Internship to
apply Python programming concepts to a real-world personal finance
management problem.

---

## Author

name: "Kaviha R. M"

degree: "B.E. Computer Science Engineering"

internship_platform: "Vault of Codes"
