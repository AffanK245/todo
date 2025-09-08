# todo.py - simple TodoList example with list function

class TodoList:
    def __init__(self):
        self.items = []

    def add(self, task):
        self.items.append(task)

    def remove(self, idx):
        if 0 <= idx < len(self.items):
            self.items.pop(idx)

    def list_tasks(self):
        if not self.items:
            return "No tasks yet!"
        return "\n".join(f"{i+1}. {t}" for i, t in enumerate(self.items))

if __name__ == "__main__":
    t = TodoList()
    t.add("Buy milk")
    t.add("Learn Git")
    t.add("Practice Python")
    print("My tasks:")
    print(t.list_tasks())
