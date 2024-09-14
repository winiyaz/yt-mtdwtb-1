# Lesson 10 - Menu Buttons

# --- Imports ---
from tkinter import *
import ttkbootstrap as tb

# --- Imports ---

# Theme setup
# Available Daark themes - solar, superhero, darkly, cyborg, vapor
root = tb.Window(themename="darkly")

# Window Setup
root.title("L10")
root.geometry("800x800")

# Main Label
main_label = tb.Label(text="L10MenuButtons", font=("Helvetica", 30))
main_label.pack(pady="20")

# --- Window Run Loop ---
root.mainloop()