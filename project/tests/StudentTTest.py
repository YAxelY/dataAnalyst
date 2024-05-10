import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import numpy as np
from scipy.stats import ttest_ind

class TTest:
    def __init__(self):
        self.dataSet1 = None
        self.dataSet2 = None
        self.alpha = 0.05
        self.t_statistic = None
        self.p_value = None

    def data_controller(self):
        # Vérifier si les données sont valides pour l'analyse
        if self.dataSet1 is not None and self.dataSet2 is not None:
            return "Les données sont valides pour l'analyse."
        else:
            return "Les données ne sont pas valides pour l'analyse."

    def test_val(self):
        # Effectuer le test t
        self.t_statistic, self.p_value = ttest_ind(self.dataSet1, self.dataSet2)

    def conclusion(self):
        # Formuler la conclusion en fonction du résultat du test
        conclusion_str = "Statistique de test t : {}\n".format(self.t_statistic)
        conclusion_str += "P-valeur : {}\n".format(self.p_value)
        if self.p_value < self.alpha:
            conclusion_str += "Conclusion : Il y a une différence significative entre les échantillons."
        else:
            conclusion_str += "Conclusion : Il n'y a pas de différence significative entre les échantillons."
        return conclusion_str

class Appt:
    def __init__(self, root):
        self.root = root
        self.root.title("Test t de Student")
        self.create_widgets()

    def create_widgets(self):
        # Frame pour l'entrée des données
        self.data_frame = ttk.LabelFrame(self.root, text="Entrée des données")
        self.data_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Label et Entry pour entrer les données du premier échantillon
        self.data1_label = ttk.Label(self.data_frame, text="Données du premier échantillon (séparées par des virgules):")
        self.data1_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.data1_entry = ttk.Entry(self.data_frame, width=50)
        self.data1_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Label et Entry pour entrer les données du deuxième échantillon
        self.data2_label = ttk.Label(self.data_frame, text="Données du deuxième échantillon (séparées par des virgules):")
        self.data2_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.data2_entry = ttk.Entry(self.data_frame, width=50)
        self.data2_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Bouton pour exécuter le test
        self.test_button = ttk.Button(self.root, text="Exécuter le test", command=self.run_test)
        self.test_button.grid(row=1, column=0, padx=10, pady=10)

        # Boutons pour ouvrir et sauvegarder des données
        self.open_button = ttk.Button(self.root, text="Ouvrir", command=self.open_data)
        self.open_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.save_button = ttk.Button(self.root, text="Sauvegarder", command=self.save_data)
        self.save_button.grid(row=1, column=1, padx=10, pady=10)

        # Frame pour afficher les résultats
        self.result_frame = ttk.LabelFrame(self.root, text="Résultats")
        self.result_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Label pour afficher les résultats
        self.result_label = ttk.Label(self.result_frame, text="")
        self.result_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    def run_test(self):
        # Récupérer les données à partir de l'entrée utilisateur
        data1_str = self.data1_entry.get()
        data2_str = self.data2_entry.get()
        try:
            self.dataSet1 = np.array(list(map(float, data1_str.split(','))))
            self.dataSet2 = np.array(list(map(float, data2_str.split(','))))
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres séparés par des virgules.")
            return
        
        # Exécuter le test t avec les données entrées
        t_test = TTest()
        t_test.dataSet1 = self.dataSet1
        t_test.dataSet2 = self.dataSet2
        t_test.test_val()
        conclusion = t_test.conclusion()

        # Afficher la conclusion dans le widget des résultats
        self.result_label.config(text=conclusion)
    
    def open_data(self):
        # Ouvrir une boîte de dialogue pour sélectionner un fichier
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers CSV", "*.csv")])
        if file_path:
            try:
                # Lire les données à partir du fichier et les afficher dans les entrées de données
                with open(file_path, 'r') as file:
                    data1, data2 = file.read().split(';')
                    self.data1_entry.delete(0, tk.END)
                    self.data1_entry.insert(0, data1)
                    self.data2_entry.delete(0, tk.END)
                    self.data2_entry.insert(0, data2)
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible d'ouvrir le fichier : {e}")

    def save_data(self):
        # Ouvrir une boîte de dialogue pour sélectionner un emplacement de sauvegarde
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])
        if file_path:
            try:
                # Écrire les données des entrées dans le fichier sélectionné
                with open(file_path, 'w') as file:
                    file.write(f"{self.data1_entry.get()};{self.data2_entry.get()}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de sauvegarder le fichier : {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = Appt(root)
    root.mainloop()
