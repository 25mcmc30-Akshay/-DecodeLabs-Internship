# Expense Tracker Project
# Developed by: Akshay Guru

expenses = []

print("=" * 40)
print("        EXPENSE TRACKER")
print("=" * 40)

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Average Expense")
    print("5. Highest Expense")
    print("6. Lowest Expense")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: ₹"))
        expenses.append(amount)
        print("Expense Added Successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. ₹{expense}")

    elif choice == "3":
        print(f"Total Expense = ₹{sum(expenses)}")

    elif choice == "4":
        if len(expenses) == 0:
            print("No expenses available.")
        else:
            avg = sum(expenses) / len(expenses)
            print(f"Average Expense = ₹{avg:.2f}")

    elif choice == "5":
        if len(expenses) == 0:
            print("No expenses available.")
        else:
            print(f"Highest Expense = ₹{max(expenses)}")

    elif choice == "6":
        if len(expenses) == 0:
            print("No expenses available.")
        else:
            print(f"Lowest Expense = ₹{min(expenses)}")

    elif choice == "7":
        print("\nThank You for using Expense Tracker!")
        break

    else:
        print("Invalid Choice!")
