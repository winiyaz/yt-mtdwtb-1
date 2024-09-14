# FloodGate and Progress bar

# --- Imports ---
from tkinter import *

import ttkbootstrap as tb

# --- Imports ---

# Theme setup
root = tb.Window(themename="solar")

# Window Setup
root.title("Lesson 7 Work")
root.geometry("800x600")

# Main Label
main_label = tb.Label(text="L7FloodGateAndProgressBar", font=("Helvetica", 30))
main_label.pack(pady="20")


# --- FloodGuageCode ---

# Functiond

def starter():
	""" start gauge"""
	my_gauge.start()


def stopper():
	""" stop gauge"""
	my_gauge.stop()


def incrementer():
	"""Incrementer"""
	my_gauge.step(20)
	label2.config(text=f"Position: {my_gauge.variable.get()}")


my_gauge = tb.Floodgauge(root, bootstyle="success", font=('Helvetica', 18),
						 mask="Pos: {}%", maximum=80, orient="horizontal", value=10,
						 )
my_gauge.pack(pady=20, fill=X, padx=20)

my_button_style = tb.Style()
my_button_style.configure('danger.TButton', font=("Helvetica", 30))

start_button = tb.Button(root, text="Start", style="danger.TButton", command=starter, width=20)
start_button.pack(pady=20)

stop_button = tb.Button(root, text="STOP", style="danger.TButton", command=stopper, width=20)
stop_button.pack(pady=20)

inc_button = tb.Button(root, text="INCR", style="danger.TButton", command=incrementer, width=20)
inc_button.pack(pady=20)

label2 = tb.Label(root, text="Position: ", font=("Helvetica", 20), bootstyle="info")
label2.pack(pady=20)

# --- Window Run Loop ---
root.mainloop()
