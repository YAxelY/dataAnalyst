import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import scipy.stats as stats
import pickle

class WilcoxonApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Test de Wilcoxon pour échantillons appariés")

        self.frame_data = tk.Frame(master, padx=20, pady=20)
        self.frame_data.grid(row=0, column=0, sticky="nsew")
        
        self.result_frame = tk.Frame(master, padx=20, pady=20)
        self.result_frame.grid(row=1, column=0, sticky="nsew")

        self.num_columns_entry = tk.Entry(master=self.frame_data, width=10)
        self.num_columns_entry.grid(row=0, column=1, padx=5, sticky="w")
        tk.Label(self.frame_data, text="Nombre de Colonnes : ").grid(row=0, column=0, padx=5, sticky="e")

        self.button_generate_table = tk.Button(master=self.frame_data, text="Générer le tableau", command=self.generate_data_table)
        self.button_generate_table.grid(row=0, column=2, padx=5, sticky="w")

        self.entries = []

        self.result_text = tk.Text(master=self.result_frame, height=15, width=60)
        self.result_text.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        self.scrollbar = ttk.Scrollbar(self.result_frame, orient="vertical", command=self.result_text.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.result_text.config(yscrollcommand=self.scrollbar.set)

        self.button_run = tk.Button(master=self.master, text="Exécuter le test", command=self.perform_wilcoxon_test)
        self.button_run.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.button_new = tk.Button(master=self.master, text="Nouveau", command=self.clear_data)
        self.button_new.grid(row=2, column=1, padx=20, pady=10, sticky="ew")
        
        self.button_save = tk.Button(master=self.master, text="Enregistrer", command=self.save_data)
        self.button_save.grid(row=2, column=2, padx=20, pady=10, sticky="ew")
        
        self.button_open = tk.Button(master=self.master, text="Ouvrir", command=self.open_data)
        self.button_open.grid(row=2, column=3, padx=20, pady=10, sticky="ew")

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

    def generate_data_table(self):
        try:
            num_columns = int(self.num_columns_entry.get())
            if num_columns <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erreur", "Le nombre de colonnes doit être un entier positif.")
            return

        self.clear_data()

        for i in range(num_columns):
            label_before = tk.Label(self.frame_data)
            label_before.grid(row=i+1, column=0, padx=5, sticky="e")
            entry_before = tk.Entry(self.frame_data)
            entry_before.grid(row=i+1, column=1, padx=5, pady=5, sticky="w")

            label_after = tk.Label(self.frame_data)
            label_after.grid(row=i+1, column=2, padx=5, sticky="e")
            entry_after = tk.Entry(self.frame_data)
            entry_after.grid(row=i+1, column=3, padx=5, pady=5, sticky="w")

            self.entries.append((entry_before, entry_after))

    def perform_wilcoxon_test(self):
        data_before = []
        data_after = []
        for entry_before, entry_after in self.entries:
            value_before = entry_before.get()
            value_after = entry_after.get()
            if value_before and value_after:
                try:
                    data_before.append(float(value_before))
                    data_after.append(float(value_after))
                except ValueError:
                    messagebox.showerror("Erreur de saisie", "Veuillez entrer uniquement des nombres.")
                    return

        if not data_before or not data_after:
            messagebox.showerror("Erreur", "Les champs de données ne doivent pas être vides.")
            return
            
        if len(data_before) != len(data_after):
            messagebox.showerror("Erreur", "Assurez-vous que chaque 'Avant' a un 'Après' correspondant.")
            return
        
        # Calcul du test de Wilcoxon
        stat, p_value = stats.wilcoxon(data_before, data_after)
        
        # Formulation
        result_text = "Résultats du Test de Wilcoxon :\n\n"
        result_text += "1. Formulation :\n"
        result_text += "   H0 : Les distributions des deux échantillons sont égales.\n"
        result_text += "   H1 : Les distributions des deux échantillons sont différentes.\n\n"
        
        # Test de probabilité à utiliser
        result_text += "2. Test de probabilité à utiliser :\n"
        result_text += "   Test de Wilcoxon pour échantillons appariés.\n\n"
        
        # Valeur observée
        result_text += "3. Valeur observée :\n"
        result_text += f"   Statistique de test : {stat}\n"
        result_text += f"   P-valeur : {p_value}\n\n"
        
        # Point critique
        result_text += "4. Point critique :\n"
        result_text += "   Niveau de signification alpha = 0.05\n\n"
        
        # Conclusion
        result_text += "5. Conclusion :\n"
        if p_value < 0.05:
            result_text += "   La p-valeur est inférieure à alpha, donc nous rejetons l'hypothèse nulle.\n"
            result_text += "   Il y a une différence statistiquement significative entre les distributions des deux échantillons.\n"
        else:
            result_text += "   La p-valeur est supérieure à alpha, donc nous ne rejetons pas l'hypothèse nulle.\n"
            result_text += "   Il n'y a pas suffisamment de preuves pour affirmer qu'il y a une différence statistiquement significative entre les distributions des deux échantillons.\n"
        
        # Afficher le résultat dans la zone de texte
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, result_text)

    def clear_data(self):
        self.result_text.delete('1.0', tk.END)
        for entry_before, entry_after in self.entries:
            entry_before.destroy()
            entry_after.destroy()
        self.entries = []
        
    def save_data(self):
        data = {
            "num_columns": self.num_columns_entry.get(),
            "entries": [(entry_before.get(), entry_after.get()) for entry_before, entry_after in self.entries]
        }
        filename = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Pickle files", "*.pkl")])
        if filename:
            with open(filename, 'wb') as file:
                pickle.dump(data, file)
                messagebox.showinfo("Enregistrement réussi", "Les données ont été enregistrées avec succès.")

    def open_data(self):
        filename = filedialog.askopenfilename(filetypes=[("Pickle files", "*.pkl")])
        if filename:
            with open(filename, 'rb') as file:
                data = pickle.load(file)
                self.num_columns_entry.delete(0, tk.END)
                self.num_columns_entry.insert(0, data["num_columns"])
                self.generate_data_table()
                for (entry_before, entry_after), (value_before, value_after) in zip(self.entries, data["entries"]):
                    entry_before.delete(0, tk.END)
                    entry_before.insert(0, value_before)
                    entry_after.delete(0, tk.END)
                    entry_after.insert(0, value_after)
                messagebox.showinfo("Ouverture réussie", "Les données ont été ouvertes avec succès.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WilcoxonApp(root)
    root.mainloop()
