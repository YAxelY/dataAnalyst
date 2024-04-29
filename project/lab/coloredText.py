import tkinter as tk
from prettytable import PrettyTable
import re

def displayFormattedText(inputString, textWidget):
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

# Create a tkinter window
root = tk.Tk()
root.title("Formatted Text Display")

# Create a text widget
text_widget = tk.Text(root, wrap="word", width=50, height=10)
text_widget.pack(fill="both", expand=True)

# Your input string
input_string = """This is a <red this text is in red>
And this is a <blue and this text in blue>"""

# Call the function
displayFormattedText(input_string, text_widget)

# Start the tkinter main loop
root.mainloop()
