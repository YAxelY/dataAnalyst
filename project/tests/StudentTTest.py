from scipy.stats import ttest_ind
import numpy as np

class StudentTTest:

    def __init__(self, data):
        self.sample1 = np.array(data[0])
        self.sample2 = np.array(data[1])
    
    def data_controller(self):
        if len(self.sample1) > 1 and len(self.sample2) > 1:
            self.statistic, self.p_value = ttest_ind(self.sample1, self.sample2)
    
    def hypothesis_formulation(self):
        return "H0: µ1 = µ2\nH1: µ1 ≠ µ2"
    
    def distribution(self):
        return "On utilise la loi de Student pour comparer les moyennes des deux échantillons."
    
    def test_value(self):
        return f"p-value: {self.p_value:.4f}"
    
    def steps(self, alpha=0.05):
        alpha = float(alpha)
        if self.p_value < alpha:
            return "Nous rejetons l'hypothèse nulle (H0). Il y a une différence significative entre les moyennes des deux échantillons."
        else:
            return "Nous n'avons pas suffisamment de preuves pour rejeter l'hypothèse nulle (H0). Les moyennes des deux échantillons sont statistiquement similaires."

    def conclusion(self, alpha=0.05, desc=""):
        alpha = float(alpha)
        if self.p_value < alpha:
            return f"Comme la p-value ({self.p_value:.4f}) est inférieure à {alpha}, nous rejetons l'hypothèse nulle (H0). Il y a une différence significative entre les moyennes des deux échantillons."
        else:
            return f"Comme la p-value ({self.p_value:.4f}) est supérieure à {alpha}, nous n'avons pas suffisamment de preuves pour rejeter l'hypothèse nulle (H0). Les moyennes des deux échantillons sont statistiquement similaires."

if __name__ == '__main__':
    pass
