# Date Picker

# --- Imports ---
from tkinter import *
import ttkbootstrap as tb

# --- Imports ---

# Theme setup
root = tb.Window(themename="solar")

# Window Setup
root.title("Lesson8DatePicker")
root.geometry("800x800")

# Main Label
main_label = tb.Label(text="L8 Date Picker", font=("Helvetica", 30))
main_label.pack(pady="20")

# --- Window Run Loop ---
root.mainloop()