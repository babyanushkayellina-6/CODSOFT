import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        
        self.tasks = []
        
        tk.Label(root, text="Enter Task:").pack(pady=5)
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack()
        
        
        frame = tk.Frame(root)
        frame.pack(pady=10)
        
        tk.Button(frame, text="Add", command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Delete", command=self.delete_task).grid(row=0, column=1, padx=5)
        
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter a task!")
    
    def delete_task(self):
        selection = self.listbox.curselection()
        if selection:
            self.listbox.delete(selection[0])

root = tk.Tk()
app = TodoApp(root)
root.mainloop()