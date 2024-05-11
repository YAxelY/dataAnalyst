import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
from scipy.stats import ttest_1samp, t
from scipy import stats

def run_hypothesis_test():
    try:
        # Collect user inputs
        n = int(entry_n.get())
        mu_0 = float(entry_mu.get())
        sigma = float(entry_sigma.get())
        X_bar = float(entry_x_bar.get())
        alpha = float(entry_alpha.get())

        # Initialize t_statistic with a default value
        t_statistic = None

        # Formulate hypotheses
        hypothese_nulle = 'La moyenne de la population est egale à la moyenne theorique'
        hypothese_alternative = 'La moyenne de la population est differente de la moyenne theorique'

        # Choose probability distribution
        if n > 30:
            # Perform hypothesis test using Z-test
            S_X_bar = sigma / (n ** 0.5)
            Z = (X_bar - mu_0) / S_X_bar

            # Calculate critical value for Z-test
            critical_value = stats.norm.ppf(1 - alpha / 2)
            INRH0 = [-critical_value, critical_value]

            # Perform decision
            if Z not in INRH0:
                result = "H0 accepted"
            else:
                result = "H0 rejected"
        else:
            # Perform hypothesis test using t-test
            ddl = n - 1
            sample_std_error = sigma / np.sqrt(n)
            t_statistic = (X_bar - mu_0) / sample_std_error

            # Calculate critical value for t-test
            critical_value = t.ppf(1 - alpha / 2, n - 1)
            INRH0 = [-critical_value, critical_value]

            # Perform decision
            if t_statistic not in INRH0:
                result = "H0 accepted"
            else:
                result = "H0 rejected"

        # Display the result
        result_message = f"Test Result:\n{result}"
        messagebox.showinfo("Result", result_message)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

def save_parameters():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            file.write(f"Sample Size (n): {entry_n.get()}\n")
            file.write(f"Theoretical Mean (μ0): {entry_mu.get()}\n")
            file.write(f"Sample Standard Deviation (σ): {entry_sigma.get()}\n")
            file.write(f"Sample Mean (X̄): {entry_x_bar.get()}\n")
            file.write(f"Significance Level (α): {entry_alpha.get()}\n")
        messagebox.showinfo("Save", "Parameters saved successfully.")

def open_parameters():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split(": ")
                if key == "Sample Size (n)":
                    entry_n.delete(0, tk.END)
                    entry_n.insert(tk.END, value)
                elif key == "Theoretical Mean (μ0)":
                    entry_mu.delete(0, tk.END)
                    entry_mu.insert(tk.END, value)
                elif key == "Sample Standard Deviation (σ)":
                    entry_sigma.delete(0, tk.END)
                    entry_sigma.insert(tk.END, value)
                elif key == "Sample Mean (X̄)":
                    entry_x_bar.delete(0, tk.END)
                    entry_x_bar.insert(tk.END, value)
                elif key == "Significance Level (α)":
                    entry_alpha.delete(0, tk.END)
                    entry_alpha.insert(tk.END, value)
        messagebox.showinfo("Open", "Parameters loaded successfully.")

# Create main window
root = tk.Tk()
root.title("Hypothesis Testing")

# Labels and entry fields
tk.Label(root, text="Sample Size (n):").grid(row=0, column=0, padx=5, pady=5)
entry_n = tk.Entry(root)
entry_n.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Theoretical Mean (μ0):").grid(row=1, column=0, padx=5, pady=5)
entry_mu = tk.Entry(root)
entry_mu.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Sample Standard Deviation (σ):").grid(row=2, column=0, padx=5, pady=5)
entry_sigma = tk.Entry(root)
entry_sigma.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Sample Mean (X̄):").grid(row=3, column=0, padx=5, pady=5)
entry_x_bar = tk.Entry(root)
entry_x_bar.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Significance Level (α):").grid(row=4, column=0, padx=5, pady=5)
entry_alpha = tk.Entry(root)
entry_alpha.grid(row=4, column=1, padx=5, pady=5)

# Buttons
btn_run_test = tk.Button(root, text="Run Test", command=run_hypothesis_test)
btn_run_test.grid(row=5, column=0, padx=5, pady=5)

btn_save = tk.Button(root, text="Save Parameters", command=save_parameters)
btn_save.grid(row=5, column=1, padx=5, pady=5)

btn_open = tk.Button(root, text="Open Parameters", command=open_parameters)
btn_open.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
