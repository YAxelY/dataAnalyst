import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class DataAnalysisApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Analysis")
        self.geometry("400x500")  # Augmenter la hauteur pour faire de la place au tableau
        
        self.create_widgets()
    
    def create_widgets(self):
        # Créer la barre de menu
        menubar = tk.Menu(self, bg="red")  # Fond rouge pour la barre de menu
        
        # Menu Fichier
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Ouvrir", command=self.open_file)
        file_menu.add_command(label="Sauvegarder", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.quit_app)
        menubar.add_cascade(label="Fichier", menu=file_menu)
        
        # Menu Paramètres
        parameters_menu = tk.Menu(menubar, tearoff=0)
        
        # Sous-menu Thème
        theme_menu = tk.Menu(parameters_menu, tearoff=0)
        theme_menu.add_command(label="Dark", command=self.set_dark_theme)
        theme_menu.add_command(label="Light", command=self.set_light_theme)
        parameters_menu.add_cascade(label="Thème", menu=theme_menu)
        
        # Sous-menu Taille
        size_menu = tk.Menu(parameters_menu, tearoff=0)
        size_menu.add_command(label="+", command=self.increase_size)
        size_menu.add_command(label="-", command=self.decrease_size)
        size_menu.add_command(label="Reintialiser", command=self.reset_size)
        parameters_menu.add_cascade(label="Taille", menu=size_menu)
        
        # Sous-menu Langue
        language_menu = tk.Menu(parameters_menu, tearoff=0)
        language_menu.add_command(label="Anglais", command=self.set_language_english)
        language_menu.add_command(label="Francais", command=self.set_language_french)
        parameters_menu.add_cascade(label="Langue", menu=language_menu)
        
        # Sous-menu Préférences
        preferences_menu = tk.Menu(parameters_menu, tearoff=0)
        preferences_menu.add_command(label="Option 1", command=self.preference_option1)
        preferences_menu.add_command(label="Option 2", command=self.preference_option2)
        parameters_menu.add_cascade(label="Préférences", menu=preferences_menu)
        
        menubar.add_cascade(label="Paramètres", menu=parameters_menu)
        
        self.config(menu=menubar)
        
        # Ajouter des onglets Input et Output
        tab_control = ttk.Notebook(self)
        tab_input = ttk.Frame(tab_control)
        tab_output = ttk.Frame(tab_control)
        tab_control.add(tab_input, text='Entree')
        tab_control.add(tab_output, text='Sortie')
        tab_control.pack(expand=1, fill="both")
        
        # Ajouter un label "Seuil de Signification" et son champ après les onglets
        label_type = ttk.Label(tab_input, text="type de test:")
        label_nature = ttk.Label(tab_input, text="Nature du test:")
        label_description = ttk.Label(tab_input, text="Enoncer:")
        label_seuil = ttk.Label(tab_input, text="Seuil de Signification:")
        
        entry_type = tk.Text(tab_input, height=3)  # Ajuster la hauteur ici
        entry_nature = tk.Text(tab_input, height=3)  # Ajuster la hauteur ici
        entry_description = tk.Text(tab_input, height=5)  # Ajuster la hauteur ici
        entry_seuil = tk.Text(tab_input, height=3)  # Ajuster la hauteur ici
        
        # Placement des labels et champs avec la méthode grid
        label_type.grid(row=0, column=0, sticky="w", padx=(10, 5), pady=(10, 0))
        entry_type.grid(row=0, column=1, sticky="w", padx=(0, 10), pady=(10, 0))
        
        label_nature.grid(row=1, column=0, sticky="w", padx=(10, 5), pady=(5, 0))
        entry_nature.grid(row=1, column=1, sticky="w", padx=(0, 10), pady=(5, 0))
        
        label_description.grid(row=2, column=0, sticky="w", padx=(10, 5), pady=(5, 0))
        entry_description.grid(row=2, column=1, sticky="w", padx=(0, 10), pady=(5, 0))
        
        label_seuil.grid(row=3, column=0, sticky="w", padx=(10, 5), pady=(5, 0))
        entry_seuil.grid(row=3, column=1, sticky="w", padx=(0, 10), pady=(5, 0))
        
        # Ajout d'un tableau en bas avec deux labels et leurs champs d'entrée respectifs
        table_frame = ttk.Frame(self)
        table_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        table_label = ttk.Label(table_frame, text="Tableau de données")
        table_label.pack(pady=(0, 5))
        
        # Création du tableau
        table = ttk.Treeview(table_frame, columns=("Label", "Valeur"), show="headings")
        table.heading("Label", text="Label")
        table.heading("Valeur", text="Valeur")
        table.pack(fill="both", expand=True)
        
        # Ajout des labels et champs dans le tableau
        table.insert("", "end", values=("Label 1", tk.Text(table, height=1)))
        table.insert("", "end", values=("Label 2", tk.Text(table, height=1)))
        
    
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
    
    # Méthodes pour les actions des menus déroulants
    
    def set_dark_theme(self):
        # Code pour définir le thème sombre
        pass
    
    def set_light_theme(self):
        # Code pour définir le thème clair
        pass
    
    def increase_size(self):
        # Code pour augmenter la taille
        pass
    
    def decrease_size(self):
        # Code pour diminuer la taille
        pass
    
    def reset_size(self):
        # Code pour réinitialiser la taille
        pass
    
    def set_language_english(self):
        # Code pour définir la langue sur l'anglais
        pass
    
    def set_language_french(self):
        # Code pour définir la langue sur le français
        pass
    
    def preference_option1(self):
        # Code pour l'option 1 des préférences
        pass
    
    def preference_option2(self):
        # Code pour l'option 2 des préférences
        pass
    
    def open_input_window(self):
        input_window = tk.Toplevel(self)
        input_window.title("Input")
        # Ajouter les éléments de l'interface pour l'onglet Input ici
    
    def open_output_window(self):
        output_window = tk.Toplevel(self)
        output_window.title("Output")
        # Ajouter les éléments de l'interface pour l'onglet Output ici

if __name__ == "__main__":
    app = DataAnalysisApp()
    app.mainloop()
