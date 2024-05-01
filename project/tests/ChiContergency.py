from scipy.stats import chi2_contingency, chi2
import tkinter as tk
from tkinter import messagebox

class ChiSquareTest:
    def init(self, master):
        self.master = master
        self.master.title("Chi-Square Test Interface")

        # Create layout
        tk.Label(master, text="Enter your contingency table data (comma-separated):").grid(row=0, column=0)
        self.data_entry = tk.Text(master, height=5, width=40)
        self.data_entry.grid(row=1, column=0, padx=10, pady=10)
        self.data_entry.insert(tk.END, "10, 20, 30\n20, 20, 20")
        
        tk.Button(master, text="Run Test", command=self.run_test).grid(row=2, column=0, pady=10)
        self.result = tk.Label(master, text="")
        self.result.grid(row=3, column=0, pady=10)

    def run_test(self):
        data_text = self.data_entry.get("1.0", tk.END)
        data = [list(map(int, line.split(','))) for line in data_text.strip().split('\n')]
        self.dataSet = data
        
        try:
            self.stat, self.p_value, self.dof, _ = chi2_contingency(self.dataSet)
            critical_value = chi2.ppf(0.95, self.dof)
            conclusion = f"Chi-Square Statistic: {self.stat:.2f}, p-value: {self.p_value:.4f}\n"
            conclusion += f"Critical value at 95% confidence: {critical_value:.2f}\n"
            if self.p_value < 0.05:
                conclusion += "Result: Significant differences found (reject H0)."
            else:
                conclusion += "Result: No significant differences found (fail to reject H0)."
            self.result.configure(text=conclusion)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if name == "main":
    root = tk.Tk()
    app = ChiSquareTest(root)
    root.mainloop()