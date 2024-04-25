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

        # Label pour le titre avec fond bleu
        title_frame = tk.Frame(self, bg="blue", height=50)
        title_frame.pack(fill=tk.X)
        title_label = tk.Label(title_frame, text="Data Analysis", font=("Helvetica", 20),bg='blue')
        title_label.pack(pady=10)

        # Sélection du type de test et du nom du test d'hypothèse sur la même ligne
        navigation_frame = tk.Frame(self, bg="lightcoral")  # Fond rouge clair
        navigation_frame.pack(fill=tk.X)

        test_type_label = tk.Label(navigation_frame, text="Type de Test:")
        test_type_label.grid(row=0, column=0, padx=10, pady=5)

        test_type_var = tk.StringVar(self)
        test_type_dropdown = tk.OptionMenu(navigation_frame, test_type_var, "Test t de Student", "Test de Wilcoxon", "Test de Chi-carré")
        test_type_dropdown.config(bg="light pink")  # Fond rouge clair
        test_type_dropdown.grid(row=0, column=1, padx=10, pady=5)

        hypothesis_test_label = tk.Label(navigation_frame, text="Nom du Test d'Hypothèse:")
        hypothesis_test_label.grid(row=0, column=2, padx=10, pady=5)

        hypothesis_test_var = tk.StringVar(self)
        hypothesis_test_dropdown = tk.OptionMenu(navigation_frame, hypothesis_test_var, "Test d'Hypothèse 1", "Test d'Hypothèse 2", "Test d'Hypothèse 3")
        hypothesis_test_dropdown.config(bg="light pink")  # Fond rouge clair
        hypothesis_test_dropdown.grid(row=0, column=3, padx=10, pady=5)

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
