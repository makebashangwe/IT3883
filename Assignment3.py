# Program Name: Assignment3.py
# Course: IT3883/Section W01
# Student Name: Makeba W.
# Assignment Number: 3
# Due Date: 06/8/2026
# Purpose: This program is for a GUI to convert miles per gallon to kilometer per liter.
# I did use the slides and https://www.w3schools.com/python/ref_module_tkinter.asp,
# https://www.geeksforgeeks.org/python/python-gui-tkinter/

import tkinter as tk


# Constant
MPG_TO_KM_PER_LITER = 0.425143707


def update_conversion(*args):
    user_input = mpg_value.get().strip()

    if user_input == "":
        result_value.set("")
        return

    try:
        mpg = float(user_input)

        km_per_liter = mpg * MPG_TO_KM_PER_LITER
        result_value.set(f"{km_per_liter:.4f} km/l")

    except ValueError:
        result_value.set("Please enter numbers only")


# Create the main window
window = tk.Tk()
window.title("MPG to KM/L Converter")
window.geometry("400x200")
window.resizable(False, False)

mpg_value = tk.StringVar()
result_value = tk.StringVar()

# Trace runs update_conversion every  the user changes the MPG input
mpg_value.trace_add("write", update_conversion)

# Title
title_label = tk.Label(
    window,
    text="Miles Per Gallon to Kilometers Per Liter",
    font=("Arial", 14, "bold")
)
title_label.pack(pady=10)

# F organize the input field
input_frame = tk.Frame(window)
input_frame.pack(pady=5)

# MPG  label
mpg_label = tk.Label(input_frame, text="Miles per Gallon:")
mpg_label.grid(row=0, column=0, padx=5, pady=5)

# MPG  box
mpg_entry = tk.Entry(input_frame, textvariable=mpg_value, width=20)
mpg_entry.grid(row=0, column=1, padx=5, pady=5)

# Frame to organize the output result
output_frame = tk.Frame(window)
output_frame.pack(pady=10)

# Result label
result_label = tk.Label(output_frame, text="Kilometers per Liter:")
result_label.grid(row=0, column=0, padx=5, pady=5)

# updates automatically as the user types
result_output = tk.Label(
    output_frame,
    textvariable=result_value,
    width=22,
    anchor="w",
    relief="sunken"
)
result_output.grid(row=0, column=1, padx=5, pady=5)

# Put the cursor inside the input box when the program opens
mpg_entry.focus()

# Start the  event loop
window.mainloop()