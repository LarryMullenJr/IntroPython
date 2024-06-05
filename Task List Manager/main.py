def add_task(task_list, task):
    task_list.append(task)
    print(f"Task '{task}' added successfully.")

def remove_task(task_list, task):
    if task in task_list:
        task_list.remove(task)
        print(f"Task '{task}' removed successfully.")
    else:
        print(f"Task '{task}' not found.")

def view_tasks(task_list):
    if task_list:
        print("\nCurrent Task List:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks found.")

def save_tasks(task_list, file_name):
    try:
        with open(file_name, 'w') as file:
            for task in task_list:
                file.write(task + '\n')
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def load_tasks(file_name):
    task_list = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                task_list.append(line.strip())
        print("Tasks loaded successfully.")
    except FileNotFoundError:
        print("No previous tasks found.")
    except Exception as e:
        print(f"Error loading tasks: {e}")
    return task_list

def main():
    task_list = load_tasks("tasks.txt")
    while True:
        print("\n*** Task List Manager ***")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task_list, task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            remove_task(task_list, task)
        elif choice == '3':
            view_tasks(task_list)
        elif choice == '4':
            save_tasks(task_list, "tasks.txt")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()