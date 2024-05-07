#graphical element
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from prettytable import PrettyTable
from tkinter import messagebox

import re

def createft(title,parent_frame):
   
    frame = tk.Frame(parent_frame)

    # Create a label with the given title
    label = tk.Label(frame, text=title)
    

    # Create a text zone
    text_zone = tk.Text(frame)

    return frame, label, text_zone

def createftredox(title,parent_frame):
   
    frame = tk.Frame(parent_frame)

    # Create a label with the given title
    label = tk.Label(frame, text=title)
    

  
   

    return frame, label



def createB(parent_widget):
    frame = ttk.Frame(parent_widget)

    # Create three buttons
    button1 = ttk.Button(frame, text="Button 1")
    button2 = ttk.Button(frame, text="Button 2")
   

    return frame, button1, button2



def update_entry_text(entry_widget, text):
    # Set the entry widget state to normal
    entry_widget.config(state="normal")
    # Clear any existing text in the entry
    entry_widget.delete(0, "end")
    # Write the provided string into the entry
    entry_widget.insert(0, text)
    # Set the entry widget state back to disabled

    
    entry_widget.config(state="readonly")
    entry_widget.config(bg="white")
    # Change the border color to a light gray
    entry_widget.config(highlightbackground="white")
    # Change the border width to 1 pixel
    entry_widget.config(highlightthickness=2)


def update_text_widget(text_widget, text):
    # Set the text widget state to normal
    text_widget.config(state="normal")
    # Clear any existing text in the text widget
    text_widget.delete(1.0, "end")
    # Write the provided string into the text widget
    text_widget.insert("end", text)
    # Set the text widget state back to disabled
    text_widget.config(state="disabled")

def validate_input(new_value):
    # Check if the new value is empty or a valid number (including decimal point)
    if new_value == "" or (new_value.replace(".", "", 1).isdigit() and new_value.count(".") <= 1):
        return True
    else:
        return False


def validate_data_z(new_value):
    # Split the new value into rows
    rows = new_value.split("\n")
    # Iterate over each row
    for row in rows:
        # Check if each part of the row contains valid floats
        for part in row.split():
            # Check if the part is a valid float
            if not all(char.isdigit() or char == '.' for char in part):
                return False
    return True


def display_formatted_text(inputString, textWidget):
    def applyColorTags(line):
        # Regular expression to find color tags
        pattern = r'<(\w+)\s+(.*?)>'
        matches = re.findall(pattern, line)
        
        # Apply color to matched text
        for match in matches:
            color, text = match
            start = line.find(f"<{color} {text}>")
            end = start + len(f"<{color} {text}>")
            textWidget.insert("end", text, color)
            line = line.replace(f"<{color} {text}>", "", 1)
        
        return line
    
    # Set up text colors
    textWidget.tag_config("red", foreground="red")
    textWidget.tag_config("blue", foreground="blue")

    # Enable the text widget
    textWidget.config(state="normal")
    # Clear the previous contents
    textWidget.delete("1.0", "end")
    
    lines = inputString.split("\n")
    for line in lines:
        if line.startswith("*") and line.endswith("*"):
            # It's a table
            tableData = line.strip("*").split("|")
            table = PrettyTable(tableData[1:-1])
            table.add_row(tableData[1:-1])
            formattedTable = table.get_string()
            textWidget.insert("end", formattedTable + "\n")
        else:
            # Check for color tags and apply color
            coloredLine = applyColorTags(line)
            # Justify the line and insert it
            textWidget.insert("end", coloredLine + "\n")
    
    # Disable the text widget
    textWidget.config(state="disabled")


def replace_content(widget1, widget2):
    # Supprimer tous les widgets enfants du premier widget
    for child in widget1.winfo_children():
        child.destroy()

    # Oublier tous les widgets enfants du second widget
    for child in widget2.winfo_children():
        child.grid_forget()

    # Ajouter le contenu du second widget au premier widget
    for child in widget2.winfo_children():
        child.grid(in_=widget1, sticky="nsew")  # Réattacher au nouveau parent

    # Mettre à jour le premier widget pour afficher le nouveau contenu
    widget1.update_idletasks()


def destroy_children(widget):
    for child in widget.winfo_children():
        print(child)
        child.destroy()
    widget.update_idletasks()

def showInfoMessage(title, message,root=None):
    messagebox.showinfo(title, message,master=root)

def showWarningMessage(title, message):
    messagebox.showwarning(title, message)

def showErrorMessage(title, message):
    messagebox.showerror(title, message)

def askQuestion(title, question):
    result = messagebox.askquestion(title, question,master=None)
    return result  # Returns 'yes' or 'no'

def askOkCancel(title, question):
    result = messagebox.askokcancel(title, question,master=None)
    return result  # Returns True or False

def askYesNo(title, question):
    result = messagebox.askyesno(title, question,master=None)
    return result  # Returns True or False

def askRetryCancel(title, question):
    result = messagebox.askretrycancel(title, question,master=None)
    return result  # Returns True or False
