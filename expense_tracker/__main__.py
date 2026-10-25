"""Small interactive demonstration using in-memory data."""

from datetime import date
from decimal import Decimal

from .budgets import budget_status
from .records import add_transaction
from .summaries import monthly_summary


def main():
    transactions = []
    print("Expense Tracker - records are kept only while this program is running.")
    while True:
        print("\n1) Add transaction  2) Monthly summary  3) Check category budget  4) Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                amount = input("Amount: ").strip()
                category = input("Category: ").strip()
                kind = input("Type (income/expense): ").strip().lower()
                when = input("Date YYYY-MM-DD (blank for today): ").strip() or date.today().isoformat()
                note = input("Note (optional): ")
                add_transaction(transactions, amount, category, kind, when, note)
                print("Transaction added.")
            except ValueError as error:
                print(f"Invalid transaction: {error}")
        elif choice == "2":
            try:
                year = int(input("Year: "))
                month = int(input("Month (1-12): "))
                summary = monthly_summary(transactions, year, month)
                print(f"Income: {summary['income']} | Expenses: {summary['expenses']} | Balance: {summary['balance']}")
                print("Expenses by category:", summary["expenses_by_category"] or "none")
            except ValueError as error:
                print(f"Invalid month or year: {error}")
        elif choice == "3":
            try:
                category = input("Category: ").strip()
                limit = input("Monthly limit: ").strip()
                year = int(input("Year: "))
                month = int(input("Month (1-12): "))
                status = budget_status(transactions, category, limit, year, month)
                print(f"Spent {status['spent']} of {status['limit']}; remaining {status['remaining']}.")
                print("Within budget." if status["within_budget"] else "Budget exceeded.")
            except ValueError as error:
                print(f"Invalid budget: {error}")
        elif choice == "4":
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
