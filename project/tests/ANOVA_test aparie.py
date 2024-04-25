import tkinter as tk
from tkinter import messagebox, scrolledtext, simpledialog, filedialog
import scipy.stats as stats

def perform_anova():
    try:
        data_groups = []
        raw_data = txt_input.get('1.0', tk.END).strip().split('\n')
        for line in raw_data:
            data = list(map(float, line.split()))
            data_groups.append(data)

        F, p = stats.f_oneway(*data_groups)
        result_text = f"F-value : {F}\nP-value : {p}\n"
        if p < 0.05:
            result_text += "Il existe une différence significative entre les groupes."
        else:
            result_text += "Aucune différence significative n'a été trouvée entre les groupes."
        lbl_results.config(text=result_text)
    
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'analyse des données : {e}")

def perform_ttest():
    try:
        data = txt_input.get('1.0', tk.END).strip().split('\n')
        if len(data) != 2:
            raise ValueError("Entrez exactement deux lignes de données pour le test t apparié.")
        
        group1 = list(map(float, data[0].split()))
        group2 = list(map(float, data[1].split()))
        t_stat, p_value = stats.ttest_rel(group1, group2)
        
        result_text = f"t-statistique : {t_stat}\nP-value : {p_value}\n"
        if p_value < 0.05:
            result_text += "Il existe une différence significative entre les groupes."
        else:
            result_text += "Aucune différence significative n'a été trouvée entre les groupes."
        lbl_results.config(text=result_text)
    
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'analyse des données : {e}")

def clear_fields():
    txt_input.delete('1.0', tk.END)
    lbl_results.config(text="")

def save_data():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(txt_input.get('1.0', tk.END))
        messagebox.showinfo("Info", "Données enregistrées avec succès!")

def open_data():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            data = file.read()
            txt_input.delete('1.0', tk.END)
            txt_input.insert('1.0', data)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Tests Statistiques - Interface Améliorée avec Menu")

# Configuration du cadre de la fenêtre
frame = tk.Frame(root, bg='light blue')
frame.pack(padx=10, pady=10, fill='both', expand=True)

# Menu
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Fichier", menu=file_menu)
file_menu.add_command(label="Ouvrir", command=open_data)
file_menu.add_command(label="Enregistrer", command=save_data)

# Instructions
instructions = tk.Label(frame, text="Entrez les données pour chaque groupe, chaque groupe sur une nouvelle ligne. Utilisez des espaces pour séparer les valeurs dans un groupe.",
                        bg='light blue', justify=tk.LEFT, wraplength=400)
instructions.pack(padx=5, pady=5)

# Zone de texte pour l'entrée des données
txt_input = scrolledtext.ScrolledText(frame, height=10, width=50)
txt_input.pack(padx=5, pady=5)

# Bouton pour exécuter l'ANOVA
btn_run_anova = tk.Button(frame, text="Exécuter l'ANOVA", command=perform_anova, bg='light green')
btn_run_anova.pack(side=tk.LEFT, padx=5, pady=5)

# Bouton pour exécuter le Test t apparié
btn_run_ttest = tk.Button(frame, text="Exécuter le Test t apparié", command=perform_ttest, bg='light green')
btn_run_ttest.pack(side=tk.LEFT, padx=5, pady=5)

# Bouton pour effacer les champs
btn_clear = tk.Button(frame, text="Effacer", command=clear_fields, bg='salmon')
btn_clear.pack(side=tk.RIGHT, padx=5, pady=5)

# Label pour afficher les résultats
lbl_results = tk.Label(frame, text="", bg='light blue', justify=tk.LEFT)
lbl_results.pack(pady=5, fill='both', expand=True)

# Lancer l'interface
root.mainloop()