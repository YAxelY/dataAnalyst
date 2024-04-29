import tkinter as tk
from tkinter import filedialog

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My App")
        
        # Create entry and text widgets
        self.entry_type = tk.Entry(root)
        self.entry_nature = tk.Entry(root)
        self.entry_desc = tk.Entry(root)
        self.entry_alpha = tk.Entry(root)
        self.entry_beta = tk.Entry(root)
        self.data_z = tk.Text(root, wrap="word", width=50, height=10)
        self.form_z = tk.Text(root, wrap="word", width=50, height=10)
        self.distro_z = tk.Text(root, wrap="word", width=50, height=10)
        self.steps_z = tk.Text(root, wrap="word", width=50, height=10)
        self.p_z = tk.Text(root, wrap="word", width=50, height=10)
        self.con_z = tk.Text(root, wrap="word", width=50, height=10)
        
        # Pack widgets
        self.entry_type.pack()
        self.entry_nature.pack()
        self.entry_desc.pack()
        self.entry_alpha.pack()
        self.entry_beta.pack()
        self.data_z.pack()
        self.form_z.pack()
        self.distro_z.pack()
        self.steps_z.pack()
        self.p_z.pack()
        self.con_z.pack()
        
        # Create menu
        menu = tk.Menu(root)
        root.config(menu=menu)
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.saveToFile)
        file_menu.add_command(label="Open", command=self.openFromFile)
        
    def saveToFile(self):
        filename = filedialog.asksaveasfilename(defaultextension=".tst", filetypes=(("Text files", "*.tst"), ("All files", "*.*")))
        if filename:
            with open(filename, "w") as f:
                entries_and_texts = [
                    self.entry_type.get(),
                    self.entry_nature.get(),
                    self.entry_desc.get(),
                    self.entry_alpha.get(),
                    self.entry_beta.get(),
                    self.data_z.get("1.0", "end-1c"),  # Get text excluding the trailing newline character
                    self.form_z.get("1.0", "end-1c"),
                    self.distro_z.get("1.0", "end-1c"),
                    self.steps_z.get("1.0", "end-1c"),
                    self.p_z.get("1.0", "end-1c"),
                    self.con_z.get("1.0", "end-1c")
                ]
                f.write("|".join(entries_and_texts))  # Join all entries with pipe delimiter
            print("File saved successfully.")

    def openFromFile(self):
        filename = filedialog.askopenfilename(filetypes=(("Text files", "*.tst"), ("All files", "*.*")))
        if filename:
            with open(filename, "r") as f:
                contents = f.read().split('|')  # Split contents by pipe delimiter
                if len(contents) == 11:  # Ensure all entries and texts are present
                    self.entry_type.delete(0, tk.END)
                    self.entry_type.insert(0, contents[0])
                    self.entry_nature.delete(0, tk.END)
                    self.entry_nature.insert(0, contents[1])
                    self.entry_desc.delete(0, tk.END)
                    self.entry_desc.insert(0, contents[2])
                    self.entry_alpha.delete(0, tk.END)
                    self.entry_alpha.insert(0, contents[3])
                    self.entry_beta.delete(0, tk.END)
                    self.entry_beta.insert(0, contents[4])
                    self.data_z.delete("1.0", tk.END)
                    self.data_z.insert("1.0", contents[5])
                    self.form_z.delete("1.0", tk.END)
                    self.form_z.insert("1.0", contents[6])
                    self.distro_z.delete("1.0", tk.END)
                    self.distro_z.insert("1.0", contents[7])
                    self.steps_z.delete("1.0", tk.END)
                    self.steps_z.insert("1.0", contents[8])
                    self.p_z.delete("1.0", tk.END)
                    self.p_z.insert("1.0", contents[9])
                    self.con_z.delete("1.0", tk.END)
                    self.con_z.insert("1.0", contents[10])
                    print("File opened successfully.")
                else:
                    print("Invalid file format.")




# Create a tkinter window
root = tk.Tk()
app = MyApp(root)
root.mainloop()
