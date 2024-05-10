import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
from scipy.stats import f_oneway, rankdata
from statsmodels.stats.multicomp import pairwise_tukeyhsd

class DuncanTest:
    def __init__(self):
        self.data = None
        self.alpha = 0.05
        self.anova_result = None
        self.posthoc_result = None

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            return True
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de charger les données : {e}")
            return False

    def save_data(self, file_path):
        try:
            self.data.to_csv(file_path, index=False)
            return True
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de sauvegarder les données : {e}")
            return False

    def perform_anova(self):
        try:
            self.anova_result = f_oneway(*[group for name, group in self.data.groupby('Group')['Value']])
            return True
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'ANOVA : {e}")
            return False

    def perform_posthoc(self):
        try:
            posthoc = pairwise_tukeyhsd(self.data['Value'], self.data['Group'])
            self.posthoc_result = posthoc.summary()
            return True
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du test post-hoc : {e}")
            return False

class DuncanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Test de Duncan")
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

        # Bouton pour charger les données
        self.load_button = ttk.Button(self.root, text="Charger les données", command=self.load_data)
        self.load_button.grid(row=1, column=0, padx=10, pady=10)

        # Bouton pour sauvegarder les données
        self.save_button = ttk.Button(self.root, text="Sauvegarder les données", command=self.save_data)
        self.save_button.grid(row=2, column=0, padx=10, pady=10)

        # Frame pour afficher les résultats de l'ANOVA
        self.anova_frame = ttk.LabelFrame(self.root, text="Résultats de l'ANOVA")
        self.anova_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        # Label pour afficher les résultats de l'ANOVA
        self.anova_label = ttk.Label(self.anova_frame, text="")
        self.anova_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Bouton pour exécuter l'ANOVA
        self.anova_button = ttk.Button(self.root, text="Exécuter l'ANOVA", command=self.run_anova)
        self.anova_button.grid(row=4, column=0, padx=10, pady=10)

        # Frame pour afficher les résultats post-hoc
        self.posthoc_frame = ttk.LabelFrame(self.root, text="Résultats du test post-hoc")
        self.posthoc_frame.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

        # Label pour afficher les résultats post-hoc
        self.posthoc_label = tk.Text(self.posthoc_frame, wrap="word", width=50, height=10)
        self.posthoc_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Bouton pour exécuter le test post-hoc
        self.posthoc_button = ttk.Button(self.root, text="Exécuter le test post-hoc", command=self.run_posthoc)
        self.posthoc_button.grid(row=6, column=0, padx=10, pady=10)

        # Créer l'instance de DuncanTest
        self.duncan_test = DuncanTest()

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers CSV", "*.csv")])
        if file_path:
            if self.duncan_test.load_data(file_path):
                messagebox.showinfo("Information", "Données chargées avec succès.")
                self.data_entry.delete(0, tk.END)
                self.data_entry.insert(0, ", ".join([f"{row['Group']}; {row['Value']}" for index, row in self.duncan_test.data.iterrows()]))

    def save_data(self):
        if self.duncan_test.data is None:
            messagebox.showwarning("Attention", "Aucune donnée à sauvegarder.")
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])
            if file_path:
                if self.duncan_test.save_data(file_path):
                    messagebox.showinfo("Information", "Données sauvegardées avec succès.")

    def run_anova(self):
        data_str = self.data_entry.get()
        try:
            data = [row.split(';') for row in data_str.split(',')]
            self.duncan_test.data = pd.DataFrame(data, columns=['Group', 'Value'])
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la lecture des données : {e}")
            return

        if self.duncan_test.perform_anova():
            self.anova_label.config(text=f"Valeur F : {self.duncan_test.anova_result.statistic:.4f}\nP-valeur : {self.duncan_test.anova_result.pvalue:.4f}")

    def run_posthoc(self):
        data_str = self.data_entry.get()
        try:
            data = [row.split(';') for row in data_str.split(',')]
            self.duncan_test.data = pd.DataFrame(data, columns=['Group', 'Value'])
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la lecture des données : {e}")
            return

        if self.duncan_test.perform_posthoc():
            self.posthoc_label.delete('1.0', tk.END)
            self.posthoc_label.insert(tk.END, self.duncan_test.posthoc_result)


if __name__ == "__main__":
    root = tk.Tk()
    app = DuncanApp(root)
    root.mainloop()
