import tkinter as tk
from tkinter import ttk

def add_row():
    table.insert("", "end", values=("", ""))

def remove_row():
    selection = table.selection()
    if selection:
        table.delete(selection)

root = tk.Tk()
root.geometry("400x300")

table_frame = ttk.Frame(root)
table_frame.pack(expand=True, fill="both")

# Create a label for the table
table_label = ttk.Label(table_frame, text="Tableau de données")
table_label.pack(pady=(0, 5))

# Create the table
table = ttk.Treeview(table_frame, columns=("Range", "Value"), show="headings")
table.heading("Range", text="Range")
table.heading("Value", text="Value")
table.pack(fill="both", expand=True)

# Add buttons for adding and removing rows
add_button = ttk.Button(root, text="Add Row", command=add_row)
add_button.pack(pady=5)

remove_button = ttk.Button(root, text="Remove Row", command=remove_row)
remove_button.pack()

root.mainloop()
