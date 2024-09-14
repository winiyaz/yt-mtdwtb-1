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
root.geometry("800x500")

# Main Label
main_label = tb.Label(text="L10MenuButtons", font=("Helvetica", 30))
main_label.pack(pady="20")

def stuff(x):
	my_menu1.config(bootstyle=x)
	my_label1.config(text=f"You Selected => {x}")

# Menu Button
my_menu1_style = tb.Style()
my_menu1_style.configure('danger.TMenubutton', font=("Helvetica", 20))
my_menu1 = tb.Menubutton(root, style="danger.TMenubutton", text="MenuStuffs", width=40)
my_menu1.pack(pady=20)

# Creating menu items
inside_menu1 = tb.Menu(my_menu1)

# Adding Items

item_var = StringVar()
for x in ['primary', 'secondary', 'danger', 'info', 'outline primary', 'outline secondary', 'outline danger', 'outline info']:
	inside_menu1.add_radiobutton(label=x, variable=item_var, command=lambda x=x: stuff(x))

# Associate inside of menu with menu button
my_menu1['menu'] = inside_menu1

# create label
my_label1 = tb.Label(root, text="", font=('Helvetica', 20))
my_label1.pack(pady=40)

# --- Window Run Loop ---
root.mainloop()