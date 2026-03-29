#Personal Expense Tracker 
from ml_model import predict_category

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    category = predict_category(name)

    expenses.append({
        "name": name,
        "amount": amount,
        "category": category
    })

    print("Predicted Category:", category)
    print("Expense added successfully\n")


def view_expenses():
    if not expenses:
        print("No expenses recorded\n")
        return

    for e in expenses:
        print(e["name"], "-", e["category"], "-", e["amount"])


def total_expense():
    total = sum(e["amount"] for e in expenses)
    print("Total Expense:", total)


while True:
    print("\nPersonal Expense Tracker (ML Based)")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Exiting program")
        break
    else:
        print("Invalid choice")
