from expense import Expense
import json

def save_expenses():
    data = []
    for e in expenses:
        data.append(e.to_dict())
    with open("data.json", "w") as f:
        json.dump(data, f)

def load_expenses():
    global expenses
    try:
        with open("data.json", "r") as f :
            data = json.load(f)
            for item in data:
                e = Expense(item["title"], item["amount"], item["category"])
                e.date = item.get("date", e.date)
                expenses.append(e)
    except FileNotFoundError:
        expenses = []

def menu():
    print("----------------Menu----------------")
    print("1. Add expense")
    print("2. Show all expenses")
    print("3. Show total spent")
    print("4. Show expenses sorted by amount")
    print("5. Show expenses by category")
    print("6. Delete expense")
    print("7. Exit")
    print("------------------------------------")
    user_choice = input(">>> ")
    print("------------------------------------")
    return user_choice

expenses = []
load_expenses()

def add_expense():
    while True:
        title = input("Expense title: ").strip()
        if title == "":
            print("Title cannot be empty!")
        else:
            break

    while True:
        try:
            amount = float(input("Amount: "))
            break
        except ValueError:
            print("Enter a valid number!")

    while True:
        category = input("Category: ").strip()
        if category == "":
            print("Category cannot be empty!")
        else:
            break

    e = Expense(title, amount, category)
    expenses.append(e)
    save_expenses()
    print(f"Expense '{title}' added on {e.date}!")

def show_expense():
    if not expenses:
        print("No expenses found!")
        return
    for x, e in enumerate(expenses, 1):
        print(f"{x}. {e.title} - ${e.amount} - {e.category} - {e.date}")

def total_spent():
    if not expenses:
        print("Total spent: $0")
        return
    total = sum(e.amount for e in expenses)
    print(f"Total spent: ${total}")

def show_expense_sorted_by_amount():
    if not expenses:
        print("No expenses found!")
        return
    sorted_exp = sorted(expenses, key=lambda x: x.amount)
    for x, e in enumerate(sorted_exp, 1):
        print(f"{x}. {e.title} - ${e.amount} - {e.category} - {e.date}")

def show_expense_by_category():
    cat = input("Enter category to filter: ")
    filtered = [e for e in expenses if e.category.lower() == cat.lower()]
    if not filtered:
        print(f"No expenses found in category {cat}")
        return
    total = sum(e.amount for e in filtered)
    for x, e in enumerate(filtered, 1):
        print(f"{x}. {e.title} - ${e.amount} - {e.category} - {e.date}")
    print(f"Total spent in {cat}: {total}")

def delete_expense():
    while True:
        if not expenses:
            print("There is no expense to delete")
            break
        show_expense()
        delete_choice = input("Which expense do you want to delete? ")
        if not delete_choice.isdigit():
            print("Type the expense number")
            continue
        delete_choice = int(delete_choice)
        if delete_choice < 1 or delete_choice > len(expenses):
            print(f"Expense {delete_choice} is not found")
            continue
        user_permission = input(f"Are you sure to delete expense number {delete_choice} ?(y/n) ")
        if user_permission == "n":
            break
        if user_permission == "y":
            expenses.pop(delete_choice - 1)
            save_expenses()
            print(f"Expense {delete_choice} successfully deleted")
            break
        else:
            print("Invalid choice")

while True:
    user_choice = menu()
    if user_choice == "1":
        add_expense()
    elif user_choice == "2":
        show_expense()
    elif user_choice == "3":
        total_spent()
    elif user_choice == "4":
        show_expense_sorted_by_amount()
    elif user_choice == "5":
        show_expense_by_category()
    elif user_choice == "6":
        delete_expense()
    elif user_choice == "7":
        break
    else:
        print("Invalid input")