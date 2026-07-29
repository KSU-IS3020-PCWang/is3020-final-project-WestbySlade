import csv
import os

data_file = "finance_data.csv"
transaction_file = []
target_budget = 0.0

def load_data():
    if not os.path.exists(data_file):
        with open(data_file, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date", "Type", "Amount", "Category", "Description"])
        return

    try:
        with open(data_file, mode="r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row["Amount"] = float(row["Amount"])
                transaction_file.append(row)
    except Exception as e:
        print(f"Error loading data: {e}")

def save_data():
    try:
        with open(data_file, mode="w", newline="") as csvfile:
            fieldnames = ["Date", "Type", "Amount", "Category", "Description"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(transaction_file)
        print("Data saved")
    except Exception as e:
        print("Error savinng data: {e}")

def input_budget():
    global target_budget
    try:
        new_budget = float(input("Enter new budget or target spending limit ($): "))
        target_budget = new_budget
        print("Target budget: ", target_budget)
    except ValueError:
        print("Invalid budget, please enter a positive numerical dollar amount")

def add_transaction():
    print("\nAdd New Transaction")
    print("1. Income")
    print("2. Expense")
    user_choice = input("Select type of transaction (1 or 2): ")

    if user_choice == "1":
        trans_type = "Income"
    elif user_choice == "2":
        trans_type = "Expense"
    else:
        print("Invalid choice\n")
        return

    amount = float(input("Enter amount: "))
    date = input("Enter date of transaction (MM-DD-YYYY): ")
    category = input("Enter category of transaction: ")
    description = input("Enter description of transaction: ")

    record = {
        "Date": date,
        "Type": trans_type,
        "Amount": amount,
        "Category": category,
        "Description": description
    }

    transaction_file.append(record)
    print("Transaction added")

def view_summary():
    print("\nFinancial Summary:")
    total_income = 0
    total_expense = 0
    for record in transaction_file:
        if record["Type"] == "Income":
            total_income += record["Amount"]
        elif record["Type"] == "Expense":
            total_expense += record["Amount"]

    balance = total_income - total_expense

    print("Total Income: ", total_income)
    print("Total Expense: ", total_expense)
    print("Total Balance: ", balance)

def view_transactions():
    if not transaction_file:
        print("No transactions found")
        return
    for record in transaction_file:
        print(
            f"{record['Date']} | {record['Type']} | {record['Category']} | {record['Amount']} | {record['Description']}")

def view_category(item=None):
    print("\nView transactions by category")
    if not transaction_file:
        print("No transactions found")
        return

    search_category = input("Enter the category you want to view: ")

    if not search_category:
        print("Invalid category")
        return

    matching_categories = [
        item for item in transaction_file
        if item["Category"].lower() == search_category.lower()
    ]

    if not matching_categories:
        print("No transactions found under category: ", search_category)
        return

    print("Showing results for category: ", search_category)

    category_total = 0.0

    for item in matching_categories:
        print(f"{item['Date']} | {item['Type']} | {item['Category']} | {item['Amount']} | {item['Description']}")

        if item['Type'] == "Income":
            category_total += item["Amount"]
        elif item['Type'] == "Expense":
            category_total -= item["Amount"]

    print("Category Net Total: ",category_total)


# --- NEW AI FEATURE: Category Spending Breakdown ---
def view_category_breakdown():
    print("\n--- Category Spending Breakdown ---")

    # Filter expenses only
    expenses = [r for r in transaction_file if r["Type"] == "Expense"]

    if not expenses:
        print("No expenses recorded yet to show a breakdown.\n")
        return

    total_expense = sum(r["Amount"] for r in expenses)

    # Group totals by category
    category_totals = {}
    for r in expenses:
        cat = r["Category"]
        category_totals[cat] = category_totals.get(cat, 0.0) + r["Amount"]

    # Sort categories by spending (highest first)
    sorted_categories = sorted(category_totals.items(), key=lambda item: item[1], reverse=True)

    print(f"Total Expenses: ${total_expense:.2f}\n")
    print(f"{'Category':<15} | {'Amount':<10} | {'Share':<8} | Visual Distribution")
    print("-" * 60)

    for cat, amt in sorted_categories:
        percentage = (amt / total_expense) * 100
        bar_len = int(percentage / 5)  # 1 block = 5%
        bar = "█" * bar_len
        print(f"{cat:<15} | ${amt:<9.2f} | {percentage:>5.1f}%  | {bar}")
    print()

def main():
    load_data()
    print("hello")
    while True:
        print("EzBudget Finance Tracker")
        print("1. Add Transaction")
        print("2. View all Transactions")
        print("3. Add Budget")
        print("4. View Summary")
        print("5. View Transactions by Category")
        print("6. View Transactions by Category")
        print("7. Save and Exit")

        choice = input("Select an option (1-7): ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            input_budget()
        elif choice == "4":
            view_summary()
        elif choice == "5":
            view_category()
        elif choice == "6":
            view_category_breakdown()
        elif choice == "7":
            save_data()
            print("Thank you for using EzBudget")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
        main()