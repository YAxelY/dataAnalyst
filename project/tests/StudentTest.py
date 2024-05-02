import numpy as np
from scipy.stats import ttest_ind, t

class StudentTest:
    def __init__(self, dataSet):
        self.dataSet = dataSet  # Nous n'avons pas besoin de convertir en array ici
        self.groups = len(dataSet)
        self.t_statistic = None
        self.p_value = None
        self.critical_value = None
        
    def datacontroller(self):
        # Vérifie si chaque groupe a au moins deux observations
        if all(len(group) >= 2 for group in self.dataSet):
            return "Les données sont valides pour l'analyse."
        else:
            return "Chaque groupe doit contenir au moins deux observations pour le test de Student."
    
    def formHyp(self):
        # Formulation de l'hypothèse : Test de l'égalité des moyennes
        return "H0: Les moyennes des groupes sont égales.\nH1: Au moins une des moyennes des groupes est différente."
    
    def distribution(self):
        # Analyse de la distribution des données
        return "Analyse de la distribution des données."
    def testval(self):
    # Effectuer le test statistique
        self.t_statistic, self.p_value = ttest_ind(*self.dataSet)
    
    # Calculer la valeur critique à partir de la distribution de Student
        df = sum(len(group) - 1 for group in self.dataSet)
        self.critical_value = t.ppf(1 - self.alpha / 2, df)
        return f"t-statistique : {self.t_statistic:.4f}, p-value : {self.p_value:.4f}"

    def steps(self, alpha):
        # Définition des étapes du test avec un niveau de signification alpha
        self.alpha = float(alpha)
        return self.formHyp()  # Affichage de l'hypothèse formulée
    
    def conclusion(self, alpha=0.05, desc=""):
        # Tirer une conclusion à partir des résultats du test
        
        alpha = float(alpha)
        desc = str(desc)
        if self.p_value < alpha:
            return "Conclusion : Les moyennes des groupes sont statistiquement différentes."
        else:
            return "Conclusion : Il n'y a pas de preuve statistique de différence significative entre les moyennes des groupes."

    def dataEntry(self):
        # Retourner les widgets utilisés pour entrer les données
        pass
    
    # Fonctions personnelles (optionnelles)
    def myFunction(self, myArg1, myArg2):
        # Méthode personnelle
        pass
