# --- Imports ---
import ttkbootstrap as tb
from datetime import date

# --- Imports ---

# Theme setup
root = tb.Window(themename="solar")

# Window Setup
root.title("Lesson8DatePicker")
root.geometry("800x800")

# Main Label
main_label = tb.Label(text="L8 Date Picker", font=("Helvetica", 30))
main_label.pack(pady="20")


# Date entry widget - Calendar Widget

def Datey():
	# Grab Date
	my_date_label.config(text=f"Piked = {my_date.entry.get()}")


my_date = tb.DateEntry(root, bootstyle="info", startdate=date(2024,1,1), firstweekday=0)
my_date.pack(pady=50)

my_date_button_style = tb.Style()
my_date_button_style.configure('danger.Outline.TButton', font=("Helvetica", 20))
my_date_button = tb.Button(root, text="GetPanty", style="danger.Outline.TButton", command=Datey)
my_date_button.pack(pady=50)

my_date_label = tb.Label(root, text="Picked-->", font=('Helvetica', 30))
my_date_label.pack(pady=50)

# --- Window Run Loop ---
root.mainloop()
