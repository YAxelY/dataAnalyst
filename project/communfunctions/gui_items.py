#graphical element
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def createft(title,parent_frame):
   
    frame = tk.Frame(parent_frame)

    # Create a label with the given title
    label = tk.Label(frame, text=title)
    

    # Create a text zone
    text_zone = tk.Text(frame)

    return frame, label, text_zone



def createB(parent_widget):
    frame = ttk.Frame(parent_widget)

    # Create three buttons
    button1 = ttk.Button(frame, text="Button 1")
    button2 = ttk.Button(frame, text="Button 2")
   

    return frame, button1, button2