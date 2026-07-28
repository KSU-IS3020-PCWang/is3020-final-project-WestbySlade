import csv
import os

data_file = "finance_data.csv"
transaction_file = []

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
        print("Error loading data: {e}")

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
        print("Invalid choice")
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



    print("Total Balance: ", balance)
    print("Total Expense: ", total_expense)
    print("Total Income: ", total_income)

def view_transactions():
    for record in transaction_file:
        print(
            f"{record['Date']} | {record['Type']} | {record['Category']} | {record['Amount']} | {record['Description']}")

def view_catagory(item=None):
    print("\nView transactions by category")
    if not transaction_file:
        print("No transactions found")
        return

    search_catagory = input("Enter the category you want to view: ")

    if not search_catagory:
        print("Invalid category")
        return

    matching_catagories = [
        item for item in transaction_file
        if item["Category"].lower() == search_catagory.lower()
    ]

    if not matching_catagories:
        print("No transactions found under catagory: ", search_catagory)
        return

    print("Showing results for category: ", search_catagory)

    category_total = 0.0

    for record in matching_catagories:
        print(f"{item['Date']} | {item['Type']} | {item['Category']} | {item['Amount']} | {item['Description']}")

        if item['Type'] == "Income":
            category_total += item["Amount"]
        elif item['Type'] == "Expense":
            category_total -= item["Amount"]

    print("Category Net Total: ",category_total)

def main():
    load_data()
    print("hello")
    while True:
        print("EzBudget Finance Tracker")
        print("1. Add Transaction")
        print("2. View all Transactions")
        print("3. Add Budget")
        print("4. View Summary")
        print("5. Save and Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            input_budget()
        elif choice == "4":
            view_summary()
        elif choice == "5":
            view_catagory()
        elif choice == "6":
            save_data()
            print("Thank you for using EzBudget")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
        main()