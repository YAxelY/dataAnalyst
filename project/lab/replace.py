import tkinter as tk

def replace_frame_content(new_content):
    # Destroy the current content of the frame
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Add the new content to the frame
    new_content()

def show_first_content():
    label = tk.Label(frame, text="First Content")
    label.pack()

def show_second_content():
    label = tk.Label(frame, text="Second Content")
    label.pack()

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

# Button to show the first content
button1 = tk.Button(root, text="Show First Content", command=lambda: replace_frame_content(show_first_content))
button1.pack(side="left")

# Button to show the second content
button2 = tk.Button(root, text="Show Second Content", command=lambda: replace_frame_content(show_second_content))
button2.pack(side="right")

root.mainloop()
