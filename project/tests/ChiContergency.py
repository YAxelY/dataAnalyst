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
    
    
    #Formulation d'hypothese
    def formHyp(self):
        self.num_categories = self.observed.shape[0]
        self.num_groups = self.observed.shape[1]

        hypothesis_string = "H0: Les proportions sont égales dans toutes les populations"
        hypothesis_string += "\nH1: Au moins une proportion diffère dans une population par rapport aux autres"

        return hypothesis_string

    def effectif_experimental(self):
        row_totals = np.sum(self.observed, axis=1)
        col_totals = np.sum(self.observed, axis=0)
        self.expected = np.outer(row_totals, col_totals) / self.total_observed
        print(self.expected)
        return self.expected
    
    def testval(self):
        # self.chi_square_statistic = np.sum((self.observed - self.expected)**2 / self.expected)
        # testVal = self.chi_square_statistic
        # print(f"Valeur du test: {testVal} ")
        # return f"Valeur du test: {testVal} "
        self.p_value = 1 - chi2.cdf(self.chi_square_statistic, self.df)
        return "La P_value : {:.4f}".format(self.p_value)
    
    
    
    #Loi de distribution utiliser
    def distribution(self):
        self.df = (self.num_categories - 1) * (self.num_groups - 1)
        ddl = self.df
        print(f"Le degre de liberte du test est {ddl}")
        return f"Comme c'est un test d'homogeneite, on utilise la loi du chi-2 au degre de liberte {ddl}"
        
    
    def steps(self, alpha):
        alpha = float(alpha)
        """Calcul de la valeur critique du test d'homogeneite de Chi-deux"""
        self.df = (self.num_categories - 1) * (self.num_groups - 1)
        ddl = self.df
        critical_value = chi2.ppf(1 - alpha, ddl)
        lower_bound_INRH0 = 0
        upper_bound_INRH0 = critical_value # Seuil critique du chi-2
        
        statistic_value = f"La valeur du test est: {self.chi_square_statistic} \n"
        critical_value_string = f"Valeur critique pour chi-2 : {critical_value:.4f}"+"\n"
        region_string = f"Zone de non-rejet : [{lower_bound_INRH0:.4f}, {upper_bound_INRH0:.4f}]" +"\n"
        p_value_string = f"Valeur p : {self.p_value:.4f}"+"\n"
        #print(statistic_value+critical_value_string+region_string+p_value_string)
        result = statistic_value+critical_value_string+region_string+p_value_string
        self.effectif_experimental()
        self.testval()
        self.distribution()
        return result    
    def conclusion(self, alpha = 0.05):
        alpha = float(alpha)
        self.p_value = 1 - chi2.cdf(self.chi_square_statistic, self.df)
        
        if self.p_value < alpha:
            return "L'hypothese nulle(H0) est rejeter. Il existe une difference significative entre les groupes"
        else:
            return "L'hypothese alternative(H1) est accepter. Il n'exite pas de difference significative entre les groupes."
    
    # Méthodes supplémentaires peuvent être ajoutées selon les besoins

# Exemple d'utilisation
observed_data = np.array([[10, 20, 30], [15, 25, 35], [20, 30, 40]])
chi_square_test = ChiSquareHomogeneityTest(observed_data)
print(chi_square_test.formHyp())
print(chi_square_test.steps(0.05))
print (chi_square_test.conclusion())