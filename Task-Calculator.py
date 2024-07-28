import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = var.get()
        
        if operation == '1':
            result = num1 + num2
        elif operation == '2':
            result = num1 - num2
        elif operation == '3':
            result = num1 * num2
        elif operation == '4':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
        elif operation == '5':
            result = num1 ** 2
        else:
            messagebox.showerror("Error", "Invalid operation choice")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def reset():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_label.config(text="Result: ")

root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

input_frame = tk.Frame(root, bg="#e6e6e6", bd=5)
input_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.2, anchor="n")

tk.Label(input_frame, text="Enter the first number:", bg="#e6e6e6", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_num1 = tk.Entry(input_frame, font=("Arial", 10))
entry_num1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Enter the second number:", bg="#e6e6e6", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_num2 = tk.Entry(input_frame, font=("Arial", 10))
entry_num2.grid(row=1, column=1, padx=10, pady=5)

operation_label = tk.Label(root, text="Choose an operation:", bg="#f0f0f0", font=("Arial", 12))
operation_label.place(relx=0.5, rely=0.35, anchor="center")
var = tk.StringVar()
var.set('1')  

operations_frame = tk.Frame(root, bg="#f0f0f0")
operations_frame.place(relx=0.5, rely=0.45, anchor="center")

operations = [
    ("Add", '1'),
    ("Subtract", '2'),
    ("Multiply", '3'),
    ("Divide", '4'),
    ("Square of the first number", '5')
]

for text, value in operations:
    tk.Radiobutton(operations_frame, text=text, variable=var, value=value, bg="#f0f0f0", font=("Arial", 10)).pack(anchor="w")

result_label = tk.Label(root, text="Result: ", bg="#f0f0f0", font=("Arial", 12, "bold"))
result_label.place(relx=0.5, rely=0.75, anchor="center")

buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.place(relx=0.5, rely=0.85, anchor="center")

calculate_button = tk.Button(buttons_frame, text="Calculate", command=calculate, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), bd=3)
calculate_button.pack(side="left", padx=20)

reset_button = tk.Button(buttons_frame, text="Reset", command=reset, bg="#f44336", fg="white", font=("Arial", 12, "bold"), bd=3)
reset_button.pack(side="left", padx=20)

root.mainloop()
