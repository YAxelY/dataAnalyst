import tkinter as tk
from tkinter import Menu, filedialog, messagebox, PhotoImage
from scipy.stats import kruskal, fisher_exact, wilcoxon, mannwhitneyu
import csv

def on_enter(e, btn, color):
    btn['background'] = color

def on_leave(e, btn, color):
    btn['background'] = color

def main():
    root = tk.Tk()
    root.title("Tests Statistiques")
    root.config(bg="#f0f0f0")  # Background color

    # Optional: Add a logo (ensure the path is correct)
    try:
        logo = PhotoImage(file="path_to_logo.png")
        logo_label = tk.Label(root, image=logo, bg="#f0f0f0")
        logo_label.image = logo
        logo_label.pack(pady=10)
    except:
        print("Logo file not found. Continuing without logo.")

    # Menu
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Ouvrir", command=lambda: ouvrir_fichier(root, frame, entries))
    filemenu.add_command(label="Sauvegarder", command=lambda: sauvegarder_fichier(entries))
    menubar.add_cascade(label="Fichier", menu=filemenu)
    root.config(menu=menubar)

    # Frame for entries
    frame = tk.Frame(root, pady=20, bg="#f0f0f0")
    frame.pack(fill=tk.BOTH, expand=True)

    entries = []

    def ajout_groupe():
        entry = tk.Entry(frame, width=50, font=('Arial', 14))
        entry.pack(pady=5)
        entries.append(entry)

    def lire_donnees():
        return [list(map(float, entry.get().split())) for entry in entries if entry.get().strip()]

    def effectuer_test(test_func, test_name):
        try:
            data = lire_donnees()
            if len(data) < 2:
                raise ValueError("Veuillez entrer des données pour au moins deux groupes.")
            stat, p_value = test_func(*data)
            afficher_resultat(test_name, stat, p_value)
        except ValueError as e:
            messagebox.showerror("Erreur de données", str(e))
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    tests = [
        (kruskal, "Kruskal-Wallis"),
        (fisher_exact, "Test de Fisher"),
        (lambda x, y: wilcoxon(x, y), "Test de Wilcoxon"),
        (lambda x, y: mannwhitneyu(x, y), "Test de Mann-Whitney")
    ]
    for func, name in tests:
        btn = tk.Button(frame, text=f"Effectuer {name}", command=lambda f=func, n=name: effectuer_test(f, n),
                        bg="#4CAF50", fg="white", font=('Arial', 12), padx=10, pady=5)
        btn.pack(pady=5)
        btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b, '#45c35e'))
        btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b, '#4CAF50'))

    ajout_btn = tk.Button(frame, text="Ajouter groupe", command=ajout_groupe, bg="#008CBA", fg="white",
                          font=('Arial', 12), padx=10, pady=5)
    ajout_btn.pack(pady=10)
    ajout_btn.bind("<Enter>", lambda e, b=ajout_btn: on_enter(e, b, '#009CDE'))
    ajout_btn.bind("<Leave>", lambda e, b=ajout_btn: on_leave(e, b, '#008CBA'))

    ajout_groupe()  # Add the first entry group by default

    root.mainloop()

def afficher_resultat(test_name, stat, p_value):
    result = f"{test_name} - Statistique: {stat:.2f}, P-value: {p_value:.3f}\n"
    result += "Statistiquement significatif." if p_value < 0.05 else "Non significatif."
    messagebox.showinfo(f"Résultats du {test_name}", result)

def ouvrir_fichier(root, frame, entries):
    filepath = filedialog.askopenfilename()
    if not filepath:
        return
    for entry in entries:
        entry.pack_forget()
        entry.destroy()
    entries.clear()
    with open(filepath, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            entry = tk.Entry(frame, width=50, font=('Arial', 14))
            entry.pack(pady=5)
            entry.insert(0, ' '.join(row))
            entries.append(entry)

def sauvegarder_fichier(entries):
    filepath = filedialog.asksaveasfilename(defaultextension="csv", filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        for entry in entries:
            data = entry.get().split()
            writer.writerow(data)

if __name__ == "__main__":
    main()