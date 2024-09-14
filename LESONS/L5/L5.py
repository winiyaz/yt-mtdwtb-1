# Combox box

from tkinter import *
import ttkbootstrap as tb

# Theme setup
root = tb.Window(themename="cyborg")

# Window Setup
root.title("Lesson 5Work")
root.geometry("800x600")

# Adding label
main_label = tb.Label(text="L5 Comboboxes", font=("Helvetica", 30))
main_label.pack(pady="20")

# Create dropdown options

my_combo_style = tb.Style()
my_combo_style.configure('success.TCombobox', font=("Helvetica", 30))

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
my_combo = tb.Combobox(root, style="success.TCombobox", values=days_of_week, width=50)
my_combo.current(1)
my_combo.pack()

# Button Command
label_changer = tb.Label(text="", font=("Helvetica", 50), bootstyle="info")
label_changer.pack(pady=50)
def Klik():
	label_changer.configure(text=f"itz {my_combo.get()}")


# Create button
butt_style = tb.Style()
butt_style.configure('success.TButton', font=("Helvetica", 18))

my_butt = tb.Button(root, text="ClickMe", style="success.TButton", width=30, command=Klik)
my_butt.pack(pady=20)


# --- Window Run Loop ---
root.mainloop()
