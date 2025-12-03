# Simple To-Do List (Adds / Removes / Shows tasks)
# Stores tasks in tasks.txt

FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for t in tasks:
            f.write(t + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added:", task)

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")

def remove_task(num):
    tasks = load_tasks()
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print("Removed:", removed)
    else:
        print("Invalid task number!")

# Simple Menu
while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        num = int(input("Task number to remove: "))
        remove_task(num)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
