import tkinter as tk
from tkinter import filedialog

class DataAnalysisApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Analysis")
        self.geometry("400x150")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Créer la barre de menu
        menubar = tk.Menu(self, bg="red")  # Fond rouge pour la barre de menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Ouvrir", command=self.open_file)
        file_menu.add_command(label="Sauvegarder", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.quit_app)
        menubar.add_cascade(label="Fichier", menu=file_menu)
        self.config(menu=menubar)

       

     
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            # Traiter le fichier ouvert
            print("Fichier ouvert :", file_path)
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            # Sauvegarder les données dans le fichier
            print("Fichier sauvegardé :", file_path)
    
    def quit_app(self):
        self.destroy()

if __name__ == "__main__":
    app = DataAnalysisApp()
    app.mainloop()
