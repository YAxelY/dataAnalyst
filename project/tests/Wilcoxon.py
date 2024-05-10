import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
from scipy.stats import wilcoxon

class WilcoxonTest:
    def __init__(self):
        self.dataSet = None
        self.alpha = 0.05
        self.statistic = None
        self.p_value = None

    def data_controller(self):
        # Vérifier si les données sont valides pour l'analyse
        if self.dataSet is not None and len(self.dataSet) >= 2:
            return "Les données sont valides pour l'analyse."
        else:
            return "Les données ne sont pas valides pour l'analyse."

    def test_val(self):
        # Effectuer le test de Wilcoxon
        self.statistic, self.p_value = wilcoxon(self.dataSet)

    def conclusion(self):
        # Formuler la conclusion en fonction du résultat du test
        conclusion_str = "Statistique de test de Wilcoxon : {}\n".format(self.statistic)
        conclusion_str += "P-valeur : {}\n".format(self.p_value)
        if self.p_value < self.alpha:
            conclusion_str += "Conclusion : Il y a une différence significative entre les échantillons."
        else:
            conclusion_str += "Conclusion : Il n'y a pas de différence significative entre les échantillons."
        return conclusion_str

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Test de Wilcoxon")
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

    def run_test(self):
        # Récupérer les données à partir de l'entrée utilisateur
        data_str = self.data_entry.get()
        try:
            self.dataSet = np.array(list(map(float, data_str.split(','))))
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres séparés par des virgules.")
            return
        
        # Exécuter le test de Wilcoxon avec les données entrées
        wilcoxon_test = WilcoxonTest()
        wilcoxon_test.dataSet = self.dataSet
        wilcoxon_test.test_val()
        conclusion = wilcoxon_test.conclusion()

        # Afficher la conclusion dans le widget des résultats
        self.result_label.config(text=conclusion)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
