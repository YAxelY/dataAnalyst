import numpy as np
from scipy.stats import ttest_ind, t

class StudentTest:
    def __init__(self, dataSet):
        self.dataSet = dataSet
        self.groups = len(dataSet)
        
    def datacontroller(self):
        # Vérifie si chaque groupe a au moins deux observations
        if all(len(group) >= 2 for group in self.dataSet):
            print("Les données sont valides pour l'analyse.")
        else:
            print("Chaque groupe doit contenir au moins deux observations pour le test de Student.")
    
    def formHyp(self):
        # Formulation de l'hypothèse : Test de l'égalité des moyennes
        return "H0: Les moyennes des groupes sont égales.\n"\
                "H1: Au moins une des moyennes des groupes est différente."
    
    def distribution(self):
        # Analyse de la distribution des données
        return " "
    
    def testval(self):
        # Effectuer le test statistique
        self.t_statistic, self.p_value = ttest_ind(*self.dataSet)
        
        # Calculer la valeur critique à partir de la distribution de Student
        df = sum(len(group) - 1 for group in self.dataSet)
        self.critical_value = t.ppf(1 - self.alpha / 2, df)
    
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
            conclusion_str += "La valeur observée de la statistique de Student: {}\n".format(round(self.t_statistic, 4))
            conclusion_str += "La valeur critique de la statistique de Student: {}\n".format(round(self.critical_value, 4))
            if self.p_value < alpha:
                conclusion_str += "Conclusion: Les moyennes des groupes sont statistiquement différentes.\n"
                conclusion_str += "La valeur observée de la statistique de Student: {}\n".format(round(self.t_statistic, 4))
                conclusion_str += "La valeur critique de la statistique de Student: {}\n".format(round(self.critical_value, 4))
            else:
                conclusion_str += "Conclusion: Il n'y a pas de preuve statistique de différence significative entre les moyennes des groupes.\n"
            return conclusion_str

    def dataEntry(self):
        # Retourner les widgets utilisés pour entrer les données
        pass
    
    # Fonctions personnelles (optionnelles)
    def myFunction(self, myArg1, myArg2):
        # Méthode personnelle
        pass


if __name__ == '__main__':
        # Exemple d'utilisation de la classe
    data = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]  # Exemple de données
    test = StudentTest(data)
    test.steps(0.05)  # Définir le niveau de signification
    test.datacontroller()
    test.testval()
    test.conclusion()