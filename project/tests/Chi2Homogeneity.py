import numpy as np
from scipy.stats import chi2

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
    
    #Controlle de donnees
    def datacontroller(self):
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

# Exemple d'utilisation

