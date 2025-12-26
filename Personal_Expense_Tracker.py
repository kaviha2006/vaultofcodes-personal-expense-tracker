# Personal Expense Tracker with Income Management
# Python Mini Project - A3 (Advanced Version)

import json
import os
import datetime

EXPENSE_FILE = "expenses.json"
PROFILE_FILE = "profile.json"

# ---------------- File Handling ----------------

def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as file:
            expenses = json.load(file)
        for i, exp in enumerate(expenses, start=1):
            exp["id"] = i
        return expenses
    return []

def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def load_profile():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as file:
            return json.load(file)
    return {"monthly_income": 0}

def save_profile(profile):
    with open(PROFILE_FILE, "w") as file:
        json.dump(profile, file, indent=4)

# ---------------- Income Management ----------------

def set_monthly_income(profile):
    try:
        income = float(input("Enter monthly income: "))
        profile["monthly_income"] = income
        save_profile(profile)
        print("Monthly income saved successfully.")
    except ValueError:
        print("Invalid amount.")

def edit_monthly_income(profile):
    print("Current monthly income:", profile["monthly_income"])
    set_monthly_income(profile)

# ---------------- Expense Operations ----------------

def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (Food/Travel/etc): ")
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

        if date_input == "":
            date = datetime.date.today().isoformat()
        else:
            datetime.datetime.strptime(date_input, "%Y-%m-%d")
            date = date_input

        expense = {
            "id": len(expenses) + 1,
            "amount": amount,
            "category": category,
            "date": date
        }

        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully.")

    except ValueError:
        print("Invalid input.")

def view_all_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\nID | Date       | Category      | Amount")
    print("------------------------------------------")
    for exp in expenses:
        print(f"{exp['id']}  | {exp['date']} | {exp['category']:<12} | {exp['amount']}")

def edit_expense(expenses):
    view_all_expenses(expenses)
    try:
        eid = int(input("Enter expense ID to edit: "))
        for exp in expenses:
            if exp["id"] == eid:
                exp["amount"] = float(input("Enter new amount: "))
                exp["category"] = input("Enter new category: ")
                save_expenses(expenses)
                print("Expense updated.")
                return
        print("Expense ID not found.")
    except ValueError:
        print("Invalid input.")

def delete_expense(expenses):
    view_all_expenses(expenses)
    try:
        eid = int(input("Enter expense ID to delete: "))
        for exp in expenses:
            if exp["id"] == eid:
                expenses.remove(exp)
                for i, e in enumerate(expenses, start=1):
                    e["id"] = i
                save_expenses(expenses)
                print("Expense deleted.")
                return
        print("Expense ID not found.")
    except ValueError:
        print("Invalid input.")

# ---------------- Financial Summary ----------------

def view_financial_summary(expenses, profile):
    total_spent = sum(exp["amount"] for exp in expenses)
    income = profile["monthly_income"]
    balance = income - total_spent

    print("\n--- Financial Summary ---")
    print("Monthly Income :", income)
    print("Total Spent    :", total_spent)
    print("Remaining      :", balance)

    if income > 0 and total_spent > (0.8 * income):
        print("Warning: You have spent more than 80% of your income!")

def category_summary(expenses):
    summary = {}
    for exp in expenses:
        summary[exp["category"]] = summary.get(exp["category"], 0) + exp["amount"]

    print("\nCategory-wise Spending:")
    for cat, amt in summary.items():
        print(cat, ":", amt)

# ---------------- Main Menu ----------------

def main():
    expenses = load_expenses()
    profile = load_profile()

    if profile["monthly_income"] == 0:
        set_monthly_income(profile)

    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. View Financial Summary")
        print("6. Category-wise Summary")
        print("7. Edit Monthly Income")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_all_expenses(expenses)
        elif choice == "3":
            edit_expense(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            view_financial_summary(expenses, profile)
        elif choice == "6":
            category_summary(expenses)
        elif choice == "7":
            edit_monthly_income(profile)
        elif choice == "8":
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice.")

# ---------------- Program Start ----------------
main()
