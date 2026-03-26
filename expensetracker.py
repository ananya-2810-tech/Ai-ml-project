#Personal Expense Tracker

expenses = []

def add_expense():
  name = input("Enter expense name: ")
  amount = float(input("Enter amount: "))
  expense = {"name": name, "amount": amount}
  expenses.append(expense)

print("Expenses added successfully!\n")

def view_expenses():
  if not expenses:
    print("No expenses recorded. \n")
    return

  print("\nYour Expenses:")
  for expense in expenses:
    print(expense["name"], ":" , expense["amount"])
    print()

def total_expense():
  total = sum(expense{"amount"} for expense in expenses)
  print("Total Expense:", total, "\n")

def main():
  while True:
    print("Personal Expense Tracker")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Show Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
      add_expense()
    elif choice == "2":
      view_expense()
    elif choice == "3":
      total_expense()
    elif choice == "4":
      print("Exiting program.")
      break
    else:
      print("Invalid choice\n")

main()
