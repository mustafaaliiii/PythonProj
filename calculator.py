# -*- coding: utf-8 -*-
"""

@author: musta
"""
import tkinter as tk
from tkinter import messagebox

# Functions for arithmetic operations
def click_button(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear_entry():
    entry.delete(0, tk.END)

def add_operation():
    global first_number
    global operation
    first_number = float(entry.get())
    operation = "add"
    entry.delete(0, tk.END)

def subtract_operation():
    global first_number
    global operation
    first_number = float(entry.get())
    operation = "subtract"
    entry.delete(0, tk.END)

def multiply_operation():
    global first_number
    global operation
    first_number = float(entry.get())
    operation = "multiply"
    entry.delete(0, tk.END)

def divide_operation():
    global first_number
    global operation
    first_number = float(entry.get())
    operation = "divide"
    entry.delete(0, tk.END)

def equal_operation():
    second_number = float(entry.get())
    entry.delete(0, tk.END)

    if operation == "add":
        entry.insert(0, first_number + second_number)
    elif operation == "subtract":
        entry.insert(0, first_number - second_number)
    elif operation == "multiply":
        entry.insert(0, first_number * second_number)
    elif operation == "divide":
        if second_number == 0:
            messagebox.showerror("Error", "Cannot divide by zero!")
        else:
            entry.insert(0, first_number / second_number)

# GUI Setup
window = tk.Tk()
window.title("Simple Calculator by Mustafa")
window.configure(bg='black')  # Set the window background to black

# Entry widget
entry = tk.Entry(window, width=35, borderwidth=5, bg='white', fg='black')
entry.grid(row=0, column=0, columnspan=4)

# Button creation with black and white color scheme
button_1 = tk.Button(window, text="1", padx=20, pady=20, command=lambda: click_button(1), bg='black', fg='white')
button_2 = tk.Button(window, text="2", padx=20, pady=20, command=lambda: click_button(2), bg='black', fg='white')
button_3 = tk.Button(window, text="3", padx=20, pady=20, command=lambda: click_button(3), bg='black', fg='white')
button_4 = tk.Button(window, text="4", padx=20, pady=20, command=lambda: click_button(4), bg='black', fg='white')
button_5 = tk.Button(window, text="5", padx=20, pady=20, command=lambda: click_button(5), bg='black', fg='white')
button_6 = tk.Button(window, text="6", padx=20, pady=20, command=lambda: click_button(6), bg='black', fg='white')
button_7 = tk.Button(window, text="7", padx=20, pady=20, command=lambda: click_button(7), bg='black', fg='white')
button_8 = tk.Button(window, text="8", padx=20, pady=20, command=lambda: click_button(8), bg='black', fg='white')
button_9 = tk.Button(window, text="9", padx=20, pady=20, command=lambda: click_button(9), bg='black', fg='white')
button_0 = tk.Button(window, text="0", padx=20, pady=20, command=lambda: click_button(0), bg='black', fg='white')

button_clear = tk.Button(window, text="Clear", padx=65, pady=20, command=clear_entry, bg='black', fg='white')
button_add = tk.Button(window, text="+", padx=20, pady=20, command=add_operation, bg='black', fg='white')
button_subtract = tk.Button(window, text="-", padx=22, pady=20, command=subtract_operation, bg='black', fg='white')
button_multiply = tk.Button(window, text="*", padx=22, pady=20, command=multiply_operation, bg='black', fg='white')
button_divide = tk.Button(window, text="/", padx=22, pady=20, command=divide_operation, bg='black', fg='white')
button_equal = tk.Button(window, text="=", padx=65, pady=20, command=equal_operation, bg='black', fg='white')

# Button layout
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_equal.grid(row=5, column=1, columnspan=2)

window.mainloop()

