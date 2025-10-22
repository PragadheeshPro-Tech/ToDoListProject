FILENAME = "tasks.txt"

def load_tasks():
    """Load tasks from the file into a list (remove duplicates)."""
    tasks = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                task = line.strip()
                if task and task not in tasks:  # avoid duplicates
                    tasks.append(task)
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        if task in tasks:
            print("Task already exists!")
        else:
            tasks.append(task)
            save_tasks(tasks)
            print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return
    print("\nTasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
