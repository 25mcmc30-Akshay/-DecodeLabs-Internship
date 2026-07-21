import os

# File name
FILE_NAME = "tasks.txt"


# Load tasks from file

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        tasks = [line.strip() for line in file]

    return tasks



# Save tasks into file

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")



# Add Task

def add_task(tasks):
    task = input("Enter new task: ")

    if task == "":
        print("Task cannot be empty.")
        return

    tasks.append(task)
    save_tasks(tasks)

    print("Task Added Successfully.")



# View Tasks

def view_tasks(tasks):

    if len(tasks) == 0:
        print("\nNo Tasks Available.\n")
        return

    print("\n------ TO DO LIST ------")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    print("------------------------")



# Delete Task

def delete_task(tasks):

    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        num = int(input("Enter task number to delete: "))

        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"{removed} Deleted Successfully.")
        else:
            print("Invalid Task Number.")

    except:
        print("Please Enter Valid Number.")



# Search Task

def search_task(tasks):

    word = input("Enter keyword: ").lower()

    found = False

    print("\nMatching Tasks:\n")

    for i, task in enumerate(tasks, start=1):

        if word in task.lower():
            print(f"{i}. {task}")
            found = True

    if not found:
        print("No Matching Task Found.")



# Main Program


tasks = load_tasks()

while True:

    print("\n========== TO DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Search Task")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        search_task(tasks)

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")