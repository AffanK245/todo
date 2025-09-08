# todo.py - simple TodoList example

class TodoList:
    def __init__(self):
        self.items = []

    def add(self, task):
        self.items.append(task)

    def remove(self, idx):
        if 0 <= idx < len(self.items):
            self.items.pop(idx)

    def __str__(self):
        return "\n".join(f"{i+1}. {t}" for i, t in enumerate(self.items))

if __name__ == "__main__":
    t = TodoList()
    t.add("Buy milk")
    t.add("Learn Git")
    print(t)
