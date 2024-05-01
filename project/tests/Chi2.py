import numpy as np
from scipy.stats import chisquare
from scipy.stats import chi2

class Chi2:
    def __init__(self, dataSet):
        self.data = dataSet
        self.n = sum([len(data) 
                    for data in dataSet])
    
    
    def datacontroller(self):
        donnees_attendues = [self.n / len(data) for data in self.data]
        donnees_obs = [len(data) for data in self.data]
        if len(self.data) > 1:
            self.p_value,_ = chisquare(donnees_obs, donnees_attendues)
            # print("Statistique du test:", stat)
            # print("Valeur p:", p_value)
        
    # Formulation des hypothèses
    def formHyp(self):
        symbol = "θ²"
        hypothesis_string = "H0: "
        for i in range(1, len(self.data) + 1):
            if i > 1:
                hypothesis_string += "="
            hypothesis_string += symbol + "_{}".format(i)
        return hypothesis_string + "\nH_1: Les données suivent une distribution normale"
    
    def distribution(self):
        return "La distribution statistique suit la loi normal"
    
    
    # Calcul de la statistique du test du chi-deux
    def chiSquare(self):
        donnees_attendues = [self.n / len(data) for data in self.data]
        donnees_obs = [len(data) for data in self.data]
        moyenne = np.mean(donnees_obs)
        
        variance = np.var(donnees_obs)
        
        donnees_attendues = [self.n * (1 / np.sqrt(2 * np.pi * variance)) * np.exp(-((x - moyenne)**2) / (2 * variance)) for x in range(len(donnees_obs))]
        self.stat_chi_carre = sum([(obs - att)**2 / att for obs, att in zip(donnees_obs, donnees_attendues)])
        # print("moyenne:", moyenne)
        # print("variance:", variance)
        # print("donnees_obs: ", donnees_obs)
        # print("Statistique du test du chi-deux:", self.stat_chi_carre)
        # print("Donnees attendues:", donnees_attendues)
        return self.stat_chi_carre
    
    
    # Détermination de la valeur critique
    def testval(self):
        p_value = 1 - chi2.cdf(self.stat_chi_carre, self.ddl)
        return "La P_value : {:.4f}".format(p_value)

    # Prise de décision
    def conclusion(self):
        if self.stat_chi_carre < self.valeur_critique:
            print("L'hypothèse nulle n'est pas rejetée. Les données suivent une distribution normale.")
        else:
            print("L'hypothèse nulle est rejetée. Les données ne suivent pas une distribution normale.")
    
    # Exécution des étapes du test
    def steps(self, alpha):
        alpha = float(alpha)
        
        # Degre de liberte
        self.ddl = len(self.data) - 1
        self.valeur_critique = chi2.ppf(alpha, self.ddl)
        
        self.chiSquare()
        self.testval()
        self.conclusion()
        
        return "Valeur critique du test {}".format(self.valeur_critique)

if __name__ == '__main__':
    pass
