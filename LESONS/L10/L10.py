# Lesson 10 - Menu Buttons

# --- Imports ---
from tkinter import *
import ttkbootstrap as tb

from LESONS.L9.L9 import my_label1

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

def stuff():
	my_label1.config(text=x)

# Menu Button
my_menu1 = tb.Menubutton(root, bootstyle="warning", text="MenuStuffs")
my_menu1.pack(pady=20)

# Creating menu items
inside_menu1 = tb.Menu(my_menu1)

# Adding Items
item_var = StringVar()
for x in ['primary', 'secondary', 'danger', 'info', 'outline primary', 'outline secondary', 'outline danger', 'outline info']:
	inside_menu1.add_radiobutton(label=x, variable=item_var, command=lambda: stuff(x))

# Associate inside of menu with menu button
my_menu1['menu'] = inside_menu1

# create label
my_label1 = tb.Label(root, text="")
my_label1.pack(pady=40)

# --- Window Run Loop ---
root.mainloop()