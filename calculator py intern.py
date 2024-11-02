import tkinter as tk
from tkinter import messagebox

# Functions for each operation
def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        display_result(result)
    except ValueError:
        display_error()

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        display_result(result)
    except ValueError:
        display_error()

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        display_result(result)
    except ValueError:
        display_error()

def divide():
    try:
        if float(entry2.get()) == 0:
            messagebox.showerror("Error", "Division by zero is not allowed.")
        else:
            result = float(entry1.get()) / float(entry2.get())
            display_result(result)
    except ValueError:
        display_error()

# Helper functions to handle display of results and errors
def display_result(result):
    result_label.config(text=f"Result: {result}", fg="green")

def display_error():
    messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.config(bg="#f0f8ff")  # Light background color

# Entry fields for numbers
tk.Label(root, text="Enter first number:", bg="#f0f8ff", fg="#333333", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root, width=15, font=("Arial", 12), bg="#e6e6fa")
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter second number:", bg="#f0f8ff", fg="#333333", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root, width=15, font=("Arial", 12), bg="#e6e6fa")
entry2.grid(row=1, column=1, padx=10, pady=5)

# Buttons for each operation with different colors
button_color = "#4682b4"
button_text_color = "#ffffff"
tk.Button(root, text="Add", command=add, bg=button_color, fg=button_text_color, font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)
tk.Button(root, text="Subtract", command=subtract, bg=button_color, fg=button_text_color, font=("Arial", 12)).grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Multiply", command=multiply, bg=button_color, fg=button_text_color, font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Divide", command=divide, bg=button_color, fg=button_text_color, font=("Arial", 12)).grid(row=3, column=1, padx=10, pady=5)

# Label to display the result
result_label = tk.Label(root, text="Result: ", bg="#f0f8ff", fg="#333333", font=("Arial", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
