import tkinter as tk

def button_click():
    text.insert("end", " Button clicked!\n", ("button_text",))

root = tk.Tk()

text = tk.Text(root)
text.pack()

# Insert some styled text
text.insert("end", "Hello, ", ("normal_text",))
text.insert("end", "world!\n", ("highlight_text",))
text.insert("end", "This is a ", ("normal_text",))
text.insert("end", "button", ("button_text",))
text.insert("end", ".\n", ("normal_text",))

# Configure tag styles
text.tag_configure("normal_text", foreground="black")
text.tag_configure("highlight_text", foreground="blue", underline=True)
text.tag_configure("button_text", foreground="green", underline=True)

# Create a button
button = tk.Button(text, text="Click me!", command=button_click)
text.window_create("end", window=button)

root.mainloop()
