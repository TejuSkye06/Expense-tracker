name = input("Enter your name: ")  # Start of the program !
age = input("Enter your age: ")

print("\nHello", name + "!")

print("Thank you for using this platform! Your money, finally under control !!")

expenses = []   # each expense will be [amount, category, description]

def add_expense():
    print("\n--- Add Expense ---")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    desc = input("Enter description: ")
    expenses.append([amount, category, desc])
    print("Expense added.\n")

def view_expenses():
    print("\n--- All Expenses ---")
    if len(expenses) == 0:
        print("No expenses yet.\n")
    else:
        for i in range(len(expenses)):
            e = expenses[i]
            print(i+1, "Amount:", e[0], "| Category:", e[1], "| Description:", e[2])
        print()

def total_expenses():
    print("\n--- Total Expenses ---")
    total = 0
    for e in expenses:
        total = total + e[0]
    print("Total spent:", total, "\n")

def category_summary():
    print("\n--- Category Summary ---")
    if len(expenses) == 0:
        print("No expenses yet.\n")
        return

    summary = {}    # cat is short variable for category
    for e in expenses:
        cat = e[1]
        amt = e[0]
        if cat in summary:
            summary[cat] = summary[cat] + amt
        else:
            summary[cat] = amt

    for cat in summary:
        print(cat, ":", summary[cat])
    print()

def highest_expense():
    print("\n--- Highest Expense ---")
    if len(expenses) == 0:
        print("No expenses yet.\n")
        return

    highest = expenses[0]
    for e in expenses:
        if e[0] > highest[0]:
            highest = e

    print("Amount:", highest[0])
    print("Category:", highest[1])
    print("Description:", highest[2], "\n")


while True:
    print("=== Daily Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category Summary")
    print("5. Highest Expense")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        highest_expense()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")