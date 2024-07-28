
import tkinter as tk
from tkinter import messagebox

def viewTasks():
    tasks_listbox.delete(0, tk.END)
    if not tasks:
        tasks_listbox.insert(tk.END, "No tasks in the to-do list.")
    else:
        for index, task in enumerate(tasks, start=1):
            tasks_listbox.insert(tk.END, f"{index}. {task}")

def addTask():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_entry.delete(0, tk.END)
        viewTasks()
        messagebox.showinfo("Success", "Task added.")
    else:
        messagebox.showwarning("Warning", "Please enter a task to add.")

def updateTask():
    selected_task_index = tasks_listbox.curselection()
    if not tasks:
        messagebox.showwarning("Warning", "No tasks to update.")
    elif not selected_task_index:
        messagebox.showwarning("Warning", "Please select a task to update.")
    else:
        task_num = selected_task_index[0]
        new_task = task_entry.get()
        if new_task:
            tasks[task_num] = new_task
            task_entry.delete(0, tk.END)
            viewTasks()
            messagebox.showinfo("Success", "Task updated.")
        else:
            messagebox.showwarning("Warning", "Please enter the new task.")

def deleteTask():
    selected_task_index = tasks_listbox.curselection()
    if not tasks:
        messagebox.showwarning("Warning", "No tasks to delete.")
    elif not selected_task_index:
        messagebox.showwarning("Warning", "Please select a task to delete.")
    else:
        task_num = selected_task_index[0]
        tasks.pop(task_num)
        viewTasks()
        messagebox.showinfo("Success", "Task deleted.")

def main():
    global tasks
    tasks = []
    root = tk.Tk()
    root.title("To-Do List Application")
    root.geometry("400x500")
    root.configure(bg="#f0f0f0")

    title_label = tk.Label(root, text="To-Do List Application", bg="#f0f0f0", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    task_entry_frame = tk.Frame(root, bg="#f0f0f0")
    task_entry_frame.pack(pady=10)
    task_entry_label = tk.Label(task_entry_frame, text="Enter a task:", bg="#f0f0f0", font=("Arial", 12))
    task_entry_label.pack(side=tk.LEFT, padx=5)
    global task_entry
    task_entry = tk.Entry(task_entry_frame, font=("Arial", 12), width=25)
    task_entry.pack(side=tk.LEFT, padx=5)

    button_frame = tk.Frame(root, bg="#f0f0f0")
    button_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Add Task", command=addTask, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), bd=3)
    add_button.grid(row=0, column=0, padx=10)

    update_button = tk.Button(button_frame, text="Update Task", command=updateTask, bg="#2196F3", fg="white", font=("Arial", 12, "bold"), bd=3)
    update_button.grid(row=0, column=1, padx=10)

    delete_button = tk.Button(button_frame, text="Delete Task", command=deleteTask, bg="#f44336", fg="white", font=("Arial", 12, "bold"), bd=3)
    delete_button.grid(row=0, column=2, padx=10)

    view_button = tk.Button(button_frame, text="View Tasks", command=viewTasks, bg="#FFC107", fg="white", font=("Arial", 12, "bold"), bd=3)
    view_button.grid(row=1, column=0, columnspan=3, pady=10)

    global tasks_listbox
    tasks_listbox = tk.Listbox(root, font=("Arial", 12), width=50, height=10)
    tasks_listbox.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
