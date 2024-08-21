import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_menu():
    
    print("\nTo-Do List Menu")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    
    print("\nTo-Do List:")
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def update_task(tasks):
    
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_index] = new_task
            print("Task updated!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):

    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            print("Task deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    
    tasks=load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
            
        elif choice == '5':
            save_tasks(tasks)
            break
            
    else:
        print("Invalid choice! Please try again.")

if __name__== "__main__":
    main()
