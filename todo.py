import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks yet!")
    else:
        print("\n📌 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks, task):
    tasks.append(task)
    print(f"➕ Task added: {task}")
    save_tasks(tasks)

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"❌ Task removed: {removed}")
        save_tasks(tasks)
    else:
        print("⚠️ Invalid task number!")

def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO APP =====")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                add_task(tasks, task)
            else:
                print("⚠️ Cannot add empty task.")
        elif choice == "3":
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to remove: ").strip()) - 1
                remove_task(tasks, num)
            except ValueError:
                print("⚠️ Please enter a valid number!")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again!")

if __name__ == "__main__":
    main()
