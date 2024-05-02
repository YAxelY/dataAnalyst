import numpy as np
from scipy.stats import bartlett, chi2

class BartlettTest:
    def __init__(self, dataSet):
        self.dataSet = np.array(dataSet)
        self.groups = len(dataSet)
        
    def datacontroller(self):
        # Vérifie si chaque groupe a au moins deux observations
        if all(len(group) >= 2 for group in self.dataSet):
            return "Les données sont valides pour l'analyse."
        else:
            return ("Chaque groupe doit contenir au moins deux observations pour le test de Bartlett.")
    
    def formHyp(self):
        # Formulation de l'hypothèse : Test de l'égalité des variances
        return "H0: Les variances des groupes sont égales.\n"\
                "H1: Au moins une des variances des groupes est différente."
    
    def distribution(self):
        # Analyse de la distribution des données
        pass
    
    def testval(self):
        # Effectuer le test statistique
        self.statistic, self.p_value = bartlett(*self.dataSet)
        
        # Calculer la valeur critique à partir de la distribution chi2
        df = self.groups - 1
        self.critical_value = chi2.ppf(1 - self.alpha, df)
    
    def steps(self, alpha):
        # Définition des étapes du test avec un niveau de signification alpha
        self.alpha = float(alpha)
        self.formHyp()  # Affichage de l'hypothèse formulée
        
    def conclusion(self, alpha=0.05, desc=""):
            """
            Return a conclusion based on the test results.

            Parameters:
                alpha (float): The significance level.
                desc (str): Description of the test.

            Returns:
                str: Conclusion based on the test results.
            """
            alpha = float(alpha)
            desc = str(desc)
            conclusion_str = ""
            conclusion_str += "La valeur observée de la statistique de Bartlett: {}\n".format(self.statistic)
            conclusion_str += "La valeur critique de la statistique de Bartlett: {}\n".format(self.critical_value)
            if self.p_value < alpha:
                conclusion_str += "Conclusion: Les variances des groupes sont statistiquement différentes.\n"
                conclusion_str += "La valeur observée de la statistique de Bartlett: {}\n".format(self.statistic)
                conclusion_str += "La valeur critique de la statistique de Bartlett: {}\n".format(self.critical_value)
            else:
                conclusion_str += "Conclusion: Il n'y a pas de preuve statistique de différence significative entre les variances des groupes.\n"
            return conclusion_str


    def dataEntry(self):
        # Retourner les widgets utilisés pour entrer les données
        pass
    
    # Fonctions personnelles (optionnelles)
    def myFunction(self, myArg1, myArg2):
        # Méthode personnelle
        pass
if __name__=="__main__":
# Exemple d'utilisation de la classe
    data = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]  # Exemple de données
    test = BartlettTest(data)
    test.steps(0.05)  # Définir le niveau de signification
    test.datacontroller()
    test.testval()
    test.conclusion()
