# calculator_ui.py
import tkinter as tk
from tkinter import messagebox
import requests

# API request function (to call backend API)
def perform_operation(operation, num1, num2):
    url = f"http://127.0.0.1:5000/calculate/{operation}/{num1}/{num2}"
    response = requests.get(url)
    return response.json()["result"]

# Function to handle button click
def on_click(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = perform_operation(operation, num1, num2)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Setting up the UI
root = tk.Tk()
root.title("Simple Calculator")

# Creating widgets
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=0, padx=10, pady=10)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=1, columnspan=3)

# Creating buttons for each operation
add_button = tk.Button(root, text="Add", command=lambda: on_click('add'))
add_button.grid(row=2, column=0)

sub_button = tk.Button(root, text="Subtract", command=lambda: on_click('subtract'))
sub_button.grid(row=2, column=1)

mul_button = tk.Button(root, text="Multiply", command=lambda: on_click('multiply'))
mul_button.grid(row=2, column=2)

div_button = tk.Button(root, text="Divide", command=lambda: on_click('divide'))
div_button.grid(row=2, column=3)

# Running the main loop
root.mainloop()

