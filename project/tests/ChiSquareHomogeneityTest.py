import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import numpy as np
from scipy.stats import chi2

class Appc:
    class ChiSquareHomogeneityTest:
        def __init__(self, observed):
            self.observed = observed
            self.num_categories = observed.shape[0]
            self.num_groups = observed.shape[1]
            self.total_observed = np.sum(observed)
            self.expected = None
            self.chi_square_statistic = None
            self.df = None
            self.p_value = None
        
        # Contrôle des données
        def data_controller(self):
            if self.num_categories > 1 and self.num_groups > 1:
                self.calculate_expected()
                self.calcul_du_chi()
                self.degre_de_liberte()
            else:
                raise ValueError("Il doit y avoir au moins deux catégories et deux groupes pour effectuer le test.")
        
        # Formulation d'hypothèse
        def formHyp(self):
            hypothesis_string = "H0: Les proportions sont égales dans toutes les populations\n"
            hypothesis_string += "H1: Au moins une proportion diffère dans une population par rapport aux autres"
            return hypothesis_string

        # Calcul des effectifs théoriques
        def calculate_expected(self):
            row_totals = np.sum(self.observed, axis=1)
            col_totals = np.sum(self.observed, axis=0)
            self.expected = np.outer(row_totals, col_totals) / self.total_observed
        
        def calcul_du_chi(self):
            self.chi_square_statistic = np.sum((self.observed - self.expected)**2 / self.expected)
            return self.chi_square_statistic
        
        # Calcul des degrés de liberté
        def degre_de_liberte(self):
            self.df = (self.num_categories - 1) * (self.num_groups - 1)
            return self.df
        
        # Test de la valeur p
        def testval(self):
            self.p_value = 1 - chi2.cdf(self.calcul_du_chi(), self.degre_de_liberte())
            return "La valeur p : {:.4f}".format(self.p_value)
        
        # Loi de distribution utilisée
        def distribution(self):
            # self.df = (self.num_categories - 1) * (self.num_groups - 1)
            return f"Comme c'est un test d'homogénéité, on utilise la loi du chi-2 avec {self.degre_de_liberte()} degrés de liberté"
        
        # Étapes du test
        def steps(self, alpha):
            alpha = float(alpha)
            self.calculate_expected()
            self.chi_square_statistic = np.sum((self.observed - self.expected)**2 / self.expected)
            # self.df = (self.num_categories - 1) * (self.num_groups - 1)
            critical_value = chi2.ppf(1 - alpha, self.degre_de_liberte())
            lower_bound_INRH0 = 0
            upper_bound_INRH0 = critical_value
            
            statistic_value = f"La valeur du test est: {self.calcul_du_chi()} \n"
            critical_value_string = f"Valeur critique pour chi-2 : {critical_value:.4f}\n"
            region_string = f"Zone de non-rejet : [{lower_bound_INRH0:.4f}, {upper_bound_INRH0:.4f}]\n"
            
            result = statistic_value + critical_value_string + region_string
            return result
        
        # Conclusion du test
        def conclusion(self, alpha=0.05):
            alpha = float(alpha)
            if self.p_value is None:
                self.calculate_expected()
                # self.chi_square_statistic = np.sum((self.observed - self.expected)**2 / self.expected)
                # self.df = (self.num_categories - 1) * (self.num_groups - 1)
                self.p_value = 1 - chi2.cdf(self.calcul_du_chi(), self.degre_de_liberte())
            
            if self.p_value < alpha:
                return "L'hypothèse nulle (H0) est rejetée. Il existe une différence significative entre les groupes."
            else:
                return "L'hypothèse alternative (H1) est accepter. Il n'existe pas de différence significative entre les groupes."
    
    def __init__(self, root):
        self.root = root
        self.root.title("Test de Chi-carré d'homogénéité")
        self.create_widgets()

    def create_widgets(self):
        # Frame pour l'entrée des données
        self.data_frame = ttk.LabelFrame(self.root, text="Entrée des données")
        self.data_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Label et Entry pour entrer les données
        self.data_label = ttk.Label(self.data_frame, text="Données (séparées par des virgules et des points-virgules pour les groupes):")
        self.data_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.data_entry = ttk.Entry(self.data_frame, width=50)
        self.data_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

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
        data_str = self.data_entry.get()
        try:
            # Convertir les données en tableau numpy
            data = [[int(val) for val in group.split(',')] for group in data_str.split(';')]
            observed = np.array(data)
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres entiers séparés par des virgules et des points-virgules pour les groupes.")
            return
        
        # Exécuter le test de chi-carré d'homogénéité avec les données entrées
        chi_square_test = self.ChiSquareHomogeneityTest(observed)
        try:
            chi_square_test.data_controller()
            steps_result = chi_square_test.steps(alpha=0.05)
            conclusion = chi_square_test.conclusion(alpha=0.05)

            # Afficher les résultats dans le widget des résultats
            self.result_label.config(text=steps_result + "\n" + conclusion)
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))
    
    def open_data(self):
        # Ouvrir une boîte de dialogue pour sélectionner un fichier
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers CSV", "*.csv")])
        if file_path:
            try:
                # Lire les données à partir du fichier et les afficher dans l'entrée de données
                with open(file_path, 'r') as file:
                    data = file.read()
                    self.data_entry.delete(0, tk.END)
                    self.data_entry.insert(0, data)
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible d'ouvrir le fichier : {e}")

    def save_data(self):
        # Ouvrir une boîte de dialogue pour sélectionner un emplacement de sauvegarde
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])
        if file_path:
            try:
                # Écrire les données de l'entrée dans le fichier sélectionné
                with open(file_path, 'w') as file:
                    file.write(self.data_entry.get())
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de sauvegarder le fichier : {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = Appc(root)
    root.mainloop()
