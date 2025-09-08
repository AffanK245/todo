# todo.py - TodoList with deadlines

class TodoList:
    def __init__(self):
        self.items = []

    def add(self, task, deadline=None):
        self.items.append((task, deadline))

    def remove(self, idx):
        if 0 <= idx < len(self.items):
            self.items.pop(idx)

    def list_tasks(self):
        if not self.items:
            return "No tasks yet!"
        return "\n".join(
            f"{i+1}. {t} (Deadline: {d if d else 'No deadline'})"
            for i, (t, d) in enumerate(self.items)
        )

if __name__ == "__main__":
    t = TodoList()
    t.add("Buy milk", "Tomorrow")
    t.add("Learn Git", "This week")
    t.add("Practice Python")  # no deadline
    print("My tasks:")
    print(t.list_tasks())
