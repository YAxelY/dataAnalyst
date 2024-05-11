import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
from scipy.stats import bartlett, chi2

class BartlettTest:
    def __init__(self):
        self.dataSet = None
        self.groups = 0
        self.alpha = 0.05
        self.statistic = None
        self.p_value = None
        self.critical_value = None

    def datacontroller(self):
        # Vérifie si chaque groupe a au moins deux observations
        if all(len(group) >= 2 for group in self.dataSet):
            return "Les données sont valides pour l'analyse."
        else:
            return "Chaque groupe doit contenir au moins deux observations pour le test de Bartlett."
    
    def formHyp(self):
        # Formulation de l'hypothèse : Test de l'égalité des variances
        return "H0: Les variances des groupes sont égales.\n"\
                "H1: Au moins une des variances des groupes est différente."
    
    def distribution(self):
        # Analyse de la distribution des données
        pass
    
    def testval(self):
        # Effectuer le test statistique
        self.statistic, self.p_value = bartlett(*self.dataSet)
        
        # Calculer la valeur critique à partir de la distribution chi2
        df = self.groups - 1
        self.critical_value = chi2.ppf(1 - self.alpha, df)
    
    def steps(self):
        # Définition des étapes du test avec un niveau de signification alpha
        self.formHyp()  # Affichage de l'hypothèse formulée
        
    def conclusion(self):
        """
        Return a conclusion based on the test results.

        Returns:
            str: Conclusion based on the test results.
        """
        conclusion_str = ""
        conclusion_str += "La valeur observée de la statistique de Bartlett: {}\n".format(self.statistic)
        conclusion_str += "La valeur critique de la statistique de Bartlett: {}\n".format(self.critical_value)
        if self.p_value < self.alpha:
            conclusion_str += "Conclusion: Les variances des groupes sont statistiquement différentes.\n"
        else:
            conclusion_str += "Conclusion: Il n'y a pas de preuve statistique de différence significative entre les variances des groupes.\n"
        return conclusion_str

class Appb:
    def __init__(self, root):
        self.root = root
        self.root.title("Test de Bartlett")
        self.create_widgets()

    def create_widgets(self):
        # Frame pour l'entrée des données
        self.data_frame = ttk.LabelFrame(self.root, text="Entrée des données")
        self.data_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Label et Entry pour entrer les données
        self.data_label = ttk.Label(self.data_frame, text="Données (séparées par des virgules):")
        self.data_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.data_entry = ttk.Entry(self.data_frame, width=50)
        self.data_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Bouton pour exécuter le test
        self.test_button = ttk.Button(self.root, text="Exécuter le test", command=self.run_test)
        self.test_button.grid(row=1, column=0, padx=10, pady=10)

        # Frame pour afficher les résultats
        self.result_frame = ttk.LabelFrame(self.root, text="Résultats")
        self.result_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Label pour afficher les résultats
        self.result_label = ttk.Label(self.result_frame, text="")
        self.result_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Menu pour ouvrir et sauvegarder
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Ouvrir", command=self.open_file)
        filemenu.add_command(label="Sauvegarder", command=self.save_file)
        menubar.add_cascade(label="Fichier", menu=filemenu)
        self.root.config(menu=menubar)

    def run_test(self):
        # Récupérer les données à partir de l'entrée utilisateur
        data_str = self.data_entry.get()
        try:
            data = [list(map(int, group.split(','))) for group in data_str.split(';')]
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres entiers séparés par des virgules.")
            return
        
        # Exécuter le test de Bartlett avec les données entrées
        bartlett_test = BartlettTest()
        bartlett_test.dataSet = np.array(data)
        bartlett_test.groups = len(data)
        bartlett_test.testval()
        conclusion = bartlett_test.conclusion()

        # Afficher la conclusion dans le widget des résultats
        self.result_label.config(text=conclusion)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                data = file.read()
                self.data_entry.delete(0, tk.END)
                self.data_entry.insert(0, data)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            data = self.data_entry.get()
            with open(file_path, "w") as file:
                file.write(data)

if __name__ == "__main__":
    root = tk.Tk()
    app = Appb(root)
    root.mainloop()
