# Lesson 9 - Frames and Labels with TTKBootStrap

# --- Imports ---
from tkinter import *
import ttkbootstrap as tb

# --- Imports ---

# Theme setup
root = tb.Window(themename="superhero")

# Window Setup
root.title("Lesson 9 Frames and Labels")
root.geometry("800x800")

# Main Label
main_label = tb.Label(text="Lesson 9 Frames and Labels", font=("Helvetica", 30))
main_label.pack(pady="20")



# --- Window Run Loop ---
root.mainloop()