#Simple calculator using the GUI interface
import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Heli prajapati simple Calculator")

# Create an entry widget to display the calculations
entry = tk.Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons for numbers and operations
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create the buttons and assign their functionality
for button_text, row, column in buttons:
    button = tk.Button(window, text=button_text, padx=40, pady=20,
                       command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=column)

# Create a clear button
clear_button = tk.Button(window, text="C", padx=40, pady=20, command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2)

# Create an equal button
equal_button = tk.Button(window, text="=", padx=40, pady=20, command=button_equal)
equal_button.grid(row=5, column=2, columnspan=2)

# Start the main loop
window.mainloop()
