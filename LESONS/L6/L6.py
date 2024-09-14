# Lesson6 - Entry Widgets

# --- Imports ---
from tkinter import *
import ttkbootstrap as tb

# --- Imports ---

# Theme setup
root = tb.Window(themename="vapor")

# Window Setup
root.title("Lesson 6 Work")
root.geometry("800x600")

# Main Label
main_label = tb.Label(text="L6 EntryBoxes", font=("Helvetica", 30))
main_label.pack(pady="20")

# Create Entry Button
def speak():
	my_entry_label.config(text=f"Typed: {my_entry.get()}")

# Entry boxes
my_entry = tb.Entry(root, font=("Helvetica", 20), width=50)
my_entry.pack(pady=50)

# Entry Button
my_entry_button_style = tb.Style()
my_entry_button_style.configure('success.TButton', font=("Helvetica", 30))

my_entry_button = tb.Button(root, bootstyle="danger", text="Kluck", command=speak, style="success.TButton")
my_entry_button.pack(pady=20)

my_entry_label = tb.Label(root, text="", font=("Helvetica", 30))
my_entry_label.pack(pady=20)



# --- Window Run Loop ---
root.mainloop()