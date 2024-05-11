import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
from scipy.stats import ttest_1samp, t
from scipy import stats

class HypothesisTestApp:
    def __init__(self, master):
        self.master = master
        master.title("Hypothesis Testing")

        # Labels and entry fields
        tk.Label(master, text="Sample Size (n):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_n = tk.Entry(master)
        self.entry_n.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(master, text="Theoretical Mean (μ0):").grid(row=1, column=0, padx=5, pady=5)
        self.entry_mu = tk.Entry(master)
        self.entry_mu.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(master, text="Sample Standard Deviation (σ):").grid(row=2, column=0, padx=5, pady=5)
        self.entry_sigma = tk.Entry(master)
        self.entry_sigma.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(master, text="Sample Mean (X̄):").grid(row=3, column=0, padx=5, pady=5)
        self.entry_x_bar = tk.Entry(master)
        self.entry_x_bar.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(master, text="Significance Level (α):").grid(row=4, column=0, padx=5, pady=5)
        self.entry_alpha = tk.Entry(master)
        self.entry_alpha.grid(row=4, column=1, padx=5, pady=5)

        # Radio buttons for test type
        self.test_type = tk.StringVar()
        self.test_type.set("two-sided")
        tk.Radiobutton(master, text="Two-Sided", variable=self.test_type, value="two-sided").grid(row=5, column=0, padx=5, pady=5)
        tk.Radiobutton(master, text="Less", variable=self.test_type, value="less").grid(row=5, column=1, padx=5, pady=5)
        tk.Radiobutton(master, text="Greater", variable=self.test_type, value="greater").grid(row=5, column=2, padx=5, pady=5)

        # Buttons
        self.btn_run_test = tk.Button(master, text="Run Test", command=self.run_hypothesis_test)
        self.btn_run_test.grid(row=6, column=0, padx=5, pady=5)

        self.btn_save = tk.Button(master, text="Save Parameters", command=self.save_parameters)
        self.btn_save.grid(row=6, column=1, padx=5, pady=5)

        self.btn_open = tk.Button(master, text="Open Parameters", command=self.open_parameters)
        self.btn_open.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    def run_hypothesis_test(self):
        try:
            # Collect user inputs
            n = int(self.entry_n.get())
            mu_0 = float(self.entry_mu.get())
            sigma = float(self.entry_sigma.get())
            X_bar = float(self.entry_x_bar.get())
            alpha = float(self.entry_alpha.get())

            # Initialize t_statistic with a default value
            t_statistic = None

            # Initialize test result message
            result_message = ""

            # Formulate hypotheses
            hypothese_nulle = 'La moyenne de la population est egale à la moyenne theorique'
            hypothese_alternative = 'La moyenne de la population est differente de la moyenne theorique'
            result_message += f"Hypothesis Formulation:\nH0: {hypothese_nulle}\nH1: {hypothese_alternative}\n\n"

            # Choose probability distribution
            if n > 30:
                # Perform hypothesis test using Z-test
                S_X_bar = sigma / (n ** 0.5)
                Z = (X_bar - mu_0) / S_X_bar

                # Calculate critical value for Z-test
                if self.test_type.get() == "two-sided":
                    critical_value = stats.norm.ppf(1 - alpha / 2)
                    INRH0 = [-critical_value, critical_value]
                elif self.test_type.get() == "less":
                    critical_value = stats.norm.ppf(alpha)
                    INRH0 = [-float("inf"), critical_value]
                elif self.test_type.get() == "greater":
                    critical_value = stats.norm.ppf(1 - alpha)
                    INRH0 = [critical_value, float("inf")]
                else:
                    raise ValueError("Invalid test type")

                # Perform decision
                if Z not in INRH0:
                    result = "H0 accepted"
                else:
                    result = "H0 rejected"

                # Construct computation steps
                computation_steps = f"Computation Steps:\nZ = (X̄ - μ) / (σ / √n)\nZ = ({X_bar} - {mu_0}) / ({sigma} / √{n})\nZ = {Z}\n"
                result_message += computation_steps

                # Construct rejection interval
                rejection_interval = f"Rejection Interval for H0: [{INRH0[0]}, {INRH0[1]}]\n"
                result_message += rejection_interval

            else:
                # Perform hypothesis test using t-test
                ddl = n - 1
                sample_std_error = sigma / np.sqrt(n)
                t_statistic = (X_bar - mu_0) / sample_std_error

                # Calculate critical value for t-test
                if self.test_type.get() == "two-sided":
                    critical_value = t.ppf(1 - alpha / 2, n - 1)
                    INRH0 = [-critical_value, critical_value]
                elif self.test_type.get() == "less":
                    critical_value = t.ppf(alpha, n - 1)
                    INRH0 = [-float("inf"), critical_value]
                elif self.test_type.get() == "greater":
                    critical_value = t.ppf(1 - alpha, n - 1)
                    INRH0 = [critical_value, float("inf")]
                else:
                    raise ValueError("Invalid test type")

                # Perform decision
                if t_statistic not in INRH0:
                    result = "H0 accepted"
                else:
                    result = "H0 rejected"

                # Construct computation steps
                computation_steps = f"Computation Steps:\nT_obs = (X̄ - μ) / (σ / √n)\nT_obs = ({X_bar} - {mu_0}) / ({sigma} / √{n})\nT_obs = {t_statistic}\n"
                result_message += computation_steps

                # Construct rejection interval
                rejection_interval = f"Rejection Interval for H0: [{INRH0[0]}, {INRH0[1]}]\n"
                result_message += rejection_interval

            # Construct result message
            result_message += f"\nTest Result: {result}\n"

            # Display the result
            messagebox.showinfo("Result", result_message)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def save_parameters(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, "w") as file:
                file.write(f"Sample Size (n): {self.entry_n.get()}\n")
                file.write(f"Theoretical Mean (μ0): {self.entry_mu.get()}\n")
                file.write(f"Sample Standard Deviation (σ): {self.entry_sigma.get()}\n")
                file.write(f"Sample Mean (X̄): {self.entry_x_bar.get()}\n")
                file.write(f"Significance Level (α): {self.entry_alpha.get()}\n")
            messagebox.showinfo("Save", "Parameters saved successfully.")

    def open_parameters(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    key, value = line.strip().split(": ")
                    if key == "Sample Size (n)":
                        self.entry_n.delete(0, tk.END)
                        self.entry_n.insert(tk.END, value)
                    elif key == "Theoretical Mean (μ0)":
                        self.entry_mu.delete(0, tk.END)
                        self.entry_mu.insert(tk.END, value)
                    elif key == "Sample Standard Deviation (σ)":
                        self.entry_sigma.delete(0, tk.END)
                        self.entry_sigma.insert(tk.END, value)
                    elif key == "Sample Mean (X̄)":
                        self.entry_x_bar.delete(0, tk.END)
                        self.entry_x_bar.insert(tk.END, value)
                    elif key == "Significance Level (α)":
                        self.entry_alpha.delete(0, tk.END)
                        self.entry_alpha.insert(tk.END, value)
            messagebox.showinfo("Open", "Parameters loaded successfully.")

if __name__=="__main__":
    root = tk.Tk()
    app = HypothesisTestApp(root)
    root.mainloop()
