"""
Author: Morgan Browning
Date: 02/23/2025
Assignment: Module 06 Programming Assignment


This program allows users to convert temperatures between Celsius and Fahrenheit using a graphical user interface (GUI). 
The user can enter a temperature, click a button to convert it, and see the result displayed on the screen.
"""

import tkinter as tk
from tkinter import messagebox

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    entry.configure(state="normal")  # Force enable input field
    temp = entry.get().strip()
    if temp == "":
        messagebox.showerror("Input Error", "Please enter a number.")
        return
    try:
        celsius = float(temp)
        fahrenheit = (9/5) * celsius + 32
        result_label.config(text=f"Result: {fahrenheit:.2f} °F")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input. Enter a number.")

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
    entry.configure(state="normal")  # Force enable input field
    temp = entry.get().strip()
    if temp == "":
        messagebox.showerror("Input Error", "Please enter a number.")
        return
    try:
        fahrenheit = float(temp)
        celsius = (5/9) * (fahrenheit - 32)
        result_label.config(text=f"Result: {celsius:.2f} °C")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input. Enter a number.")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")

# Frame for layout
frame = tk.Frame(root)
frame.pack(pady=20)

# Input field
entry_label = tk.Label(frame, text="Enter Temperature:")
entry_label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(frame, width=10)  # Entry field for user input
entry.grid(row=0, column=1, padx=5, pady=5)
entry.configure(state="normal")  # FORCE ENABLE ENTRY FIELD
entry.focus_set()  # FORCE FOCUS ON INPUT FIELD

# Buttons
c_to_f_button = tk.Button(frame, text="Celsius to Fahrenheit", command=celsius_to_fahrenheit)
c_to_f_button.grid(row=1, column=0, columnspan=2, pady=5)

f_to_c_button = tk.Button(frame, text="Fahrenheit to Celsius", command=fahrenheit_to_celsius)
f_to_c_button.grid(row=2, column=0, columnspan=2, pady=5)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
