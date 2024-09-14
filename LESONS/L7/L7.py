# FloodGate and Progress bar

# --- Imports ---
from tkinter import *

import ttkbootstrap as tb

# --- Imports ---

# Theme setup
root = tb.Window(themename="solar")

# Window Setup
root.title("Lesson 7 Work")
root.geometry("800x800")

# Main Label
main_label = tb.Label(text="L7FloodGateAndProgressBar", font=("Helvetica", 30))
main_label.pack(pady="20")

# --- Main Code here ---


# --- FloodGuageCode ---

#Functiond

def starter():
	pass

def stopper():
	pass

def incrementer():
	pass



my_gauge = tb.Floodgauge(root, bootstyle="success", font=('Helvetica', 18),
						 mask="Pos: {}%", maximum=80, orient="horizontal", value=10
						 )
my_gauge.pack(pady=20, fill=X, padx=20)


my_button_style = tb.Style()
my_button_style.configure('danger.TButton', font=("Helvetica", 30))

start_button = tb.Button(root, text="Start", bootstyle="danger outline", command=starter, width=40)
start_button.pack(pady=20)

stop_button = tb.Button(root, text="STOP", bootstyle="danger outline", command=stopper, width=40)
stop_button.pack(pady=20)

inc_button = tb.Button(root, text="INCR", bootstyle="danger outline", command=incrementer, width=40)
inc_button.pack(pady=20)

# --- Window Run Loop ---
root.mainloop()
