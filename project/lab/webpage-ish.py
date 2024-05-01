import tkinter as tk

def left_button_click():
    text.insert("end", " Left button clicked!\n", ("button_text",))

def right_button_click():
    text.insert("end", " Right button clicked!\n", ("button_text",))

root = tk.Tk()

text = tk.Text(root)
text.pack(expand=True, fill="both")

# Insert some styled text
text.insert("end", "Welcome to My Webpage\n\n", ("title_text",))
text.insert("end", "This is a paragraph of text. ", ("normal_text",))
text.insert("end", "Click the buttons below!\n", ("highlight_text",))

# Configure tag styles
text.tag_configure("title_text", foreground="blue", font=("Helvetica", 16, "bold"))
text.tag_configure("normal_text", foreground="black", font=("Helvetica", 12))
text.tag_configure("highlight_text", foreground="green", font=("Helvetica", 12, "italic"))

# Create left button
left_button = tk.Button(text, text="Left Button", command=left_button_click)
text.window_create("3.0", window=left_button)

# Create right button
right_button = tk.Button(text, text="Right Button", command=right_button_click)
text.window_create("4.0", window=right_button)

root.mainloop()
