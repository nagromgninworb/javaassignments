import tkinter as tk
from tkinter import messagebox

# Function to open Workout Plans window
def open_workout_plans():
    messagebox.showinfo("Workout Plans", "This feature will allow users to create and view workout plans.")

# Function to open Workout Logs window
def open_workout_logs():
    messagebox.showinfo("Workout Logs", "This feature will allow users to log completed workouts.")

# Function to open Settings window
def open_settings():
    messagebox.showinfo("Settings", "This feature will allow users to modify app preferences.")

# Create main application window
root = tk.Tk()
root.title("Workout Planner")
root.geometry("400x300")

# Main Label
title_label = tk.Label(root, text="Workout Planner", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# Buttons to navigate
tk.Button(root, text="Workout Plans", command=open_workout_plans, width=20).pack(pady=5)
tk.Button(root, text="Workout Logs", command=open_workout_logs, width=20).pack(pady=5)
tk.Button(root, text="Settings", command=open_settings, width=20).pack(pady=5)

# Run the application
root.mainloop()
