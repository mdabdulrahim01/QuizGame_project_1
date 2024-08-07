import csv
from datetime import datetime
import matplotlib.pyplot as plt      # type: ignore

# Function to add an expense
def add_expense(amount, category, description):
    date = datetime.now().strftime("%Y-%m-%d")
    expense = [date, amount, category, description]
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(expense)

# Function to read expenses
def read_expenses():
    expenses = []
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            expenses.append(row)
    return expenses

# Function to edit an expense
def edit_expense(index, new_amount, new_category, new_description):
    expenses = read_expenses()
    if 0 <= index < len(expenses):
        expenses[index] = [expenses[index][0], new_amount, new_category, new_description]
        with open('expenses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(expenses)
        print("Expense updated successfully.")
    else:
        print("Invalid index.")

# Function to delete an expense
def delete_expense(index):
    expenses = read_expenses()
    if 0 <= index < len(expenses):
        expenses.pop(index)
        with open('expenses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(expenses)
        print("Expense deleted successfully.")
    else:
        print("Invalid index.")

# Function to search expenses
def search_expenses(keyword):
    expenses = read_expenses()
    results = [expense for expense in expenses if keyword.lower() in expense[2].lower() or keyword.lower() in expense[3].lower()]
    return results

# Function to summarize expenses by category
def summarize_by_category():
    expenses = read_expenses()
    summary = {}
    for expense in expenses:
        category = expense[2]
        amount = float(expense[1])
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    return summary

# Function to plot expenses by category
def plot_expenses_by_category():
    summary = summarize_by_category()
    categories = list(summary.keys())
    amounts = list(summary.values())
    plt.figure(figsize=(10, 5))
    plt.bar(categories, amounts)
    plt.xlabel('Categories')
    plt.ylabel('Amount Spent')
    plt.title('Expenses by Category')
    plt.show()

def main_menu():
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Search Expenses")
        print("6. View Summary by Category")
        print("7. Plot Expenses by Category")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(amount, category, description)
        elif choice == '2':
            print(read_expenses())
        elif choice == '3':
            index = int(input("Enter index of expense to edit: "))
            new_amount = float(input("Enter new amount: "))
            new_category = input("Enter new category: ")
            new_description = input("Enter new description: ")
            edit_expense(index, new_amount, new_category, new_description)
        elif choice == '4':
            index = int(input("Enter index of expense to delete: "))
            delete_expense(index)
        elif choice == '5':
            keyword = input("Enter keyword to search: ")
            print(search_expenses(keyword))
        elif choice == '6':
            print(summarize_by_category())
        elif choice == '7':
            plot_expenses_by_category()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

