import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Entry field for new task
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Buttons
        tk.Button(root, text="Add Task", width=20, command=self.add_task).pack()
        tk.Button(root, text="Delete Task", width=20, command=self.delete_task).pack()
        tk.Button(root, text="Mark as Done", width=20, command=self.mark_done).pack()

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected)
            self.save_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            task = self.task_listbox.get(selected)
            if not task.endswith("✓"):
                self.task_listbox.delete(selected)
                self.task_listbox.insert(selected, task + " ✓")
                self.save_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

    def save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            for i in range(self.task_listbox.size()):
                f.write(self.task_listbox.get(i) + "\n")

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                for line in f:
                    self.task_listbox.insert(tk.END, line.strip())

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
