#!/usr/bin/env python
# coding: utf-8

# In[8]:


#task 1 to do list
import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=20)
        
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack()
        
        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack()
        
        edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        edit_button.pack()
        
        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack()
        
        self.load_tasks()
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    
    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            edited_task = self.task_entry.get()
            if edited_task:
                self.tasks[selected_task_index] = edited_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, edited_task)
                self.task_entry.delete(0, tk.END)
                self.save_tasks()
            else:
                messagebox.showwarning("Warning", "Please enter a task.")
    
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
            self.save_tasks()
    
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
    
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    task = line.strip()
                    self.tasks.append(task)
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

