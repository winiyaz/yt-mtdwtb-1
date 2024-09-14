# Lesson 9 - Frames and Labels with TTKBootStrap

# --- Imports ---
import ttkbootstrap as tb
from tkinter import *

# --- Imports ---

# Theme setup
root = tb.Window(themename="superhero")

# Window Setup
root.title("Lesson 9 Frames and Labels")
root.geometry("800x600")

# Main Label
main_label = tb.Label(text="Lesson 9 Frames and Labels", font=("Helvetica", 30))
main_label.pack(pady="20")

def Thing():
	pass

# Frame
my_frame1 = tb.Frame(root, bootstyle="light")
my_frame1.pack(pady=40)

my_entry1 = tb.Entry(my_frame1, font=('helvetica', 20))
my_entry1.pack(pady=20, padx=20)

my_button1 = tb.Button(my_frame1, text="ClickMe", bootstyle="dark", command=Thing)
my_button1.pack(pady=20, padx=20)

my_label1 = tb.Label(root, text="HeyHey", font=('Arial', 20), bootstyle=" inverse light")
my_label1.pack(pady=20)


# --- Window Run Loop ---
root.mainloop()
