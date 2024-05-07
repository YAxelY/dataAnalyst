import numpy as np
from scipy.stats import chi2_contingency, chi2

class CochranTest:
    def __init__(self, dataSet):
        self.dataSet = np.array(dataSet)
        self.groups = len(dataSet)
        
    def datacontroller(self):
        if all(len(group) >= 2 for group in self.dataSet):
            return "Les données sont valides pour l'analyse."
        else:
            return "Chaque groupe doit contenir au moins deux observations pour le test de Cochran."
    
    def formHyp(self):
        return "H0: Les variances des groupes sont égales.\nH1: Au moins une des variances des groupes est différente."
        
    def distribution(self):
        return "Pas besoin d'analyser la distribution des données pour le test de Cochran."
        
    def testval(self):
      result = chi2_contingency(self.dataSet)
      return "Résultat du test de Cochran : " + str(result)

    def steps(self, alpha):
        # Définir les étapes du test avec le niveau de signification alpha
        self.alpha = float(alpha)
        return self.formHyp()  # Retourner l'hypothèse formulée
        
    def conclusion(self, alpha=0.05, desc=""):
        # Tirer une conclusion à partir des résultats du test
        alpha = float(alpha)
        desc = str(desc)
        conclusion = ""
        if self.p_value < alpha:
            conclusion = "Conclusion: Au moins une variance des groupes est différente."
        else:
            conclusion = "Conclusion: Il n'y a pas de preuve statistique de différence significative entre les variances des groupes."
        return conclusion
    
    def dataEntry(self):
        # Retourner les widgets utilisés pour entrer les données si nécessaire
        pass
    
    # Fonctions personnelles (optionnelles)
    def myFunction(self, myArg1, myArg2):
        # Méthode personnelle si nécessaire
        pass
if __name__=="__main__":
# Exemple d'utilisation de la classe CochranTest
 data = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]  # Exemple de données

# Création d'une instance de CochranTest
test = CochranTest(data)

# Appel des méthodes pour tester la classe
print("Contrôle des données:", test.datacontroller())
print("Hypothèses formulées:", test.steps(0.05))
print("Résultats du test de Cochran:")
print(test.testval())
print("Conclusion:", test.conclusion())
