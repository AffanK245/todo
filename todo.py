tasks = []

def show_tasks():
    if not tasks:
        print("✅ No tasks yet!")
    else:
        print("\n📌 Your Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

def add_task(task):
    tasks.append(task)
    print(f"➕ Task added: {task}")

def main():
    while True:
        print("\n===== TO-DO APP =====")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                add_task(task)
            else:
                print("⚠️ Cannot add empty task.")
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again!")

if __name__ == "__main__":
    main()
