import numpy as np
from statsmodels.stats.proportion import proportions_ztest

class TwoProportionsTest:
    def __init__(self, dataset):
        self.data = dataset
       
        
    def datacontroller(self, proportion1=0, proportion2=0):
        self.dataset=self.data[0]
        self.proportion1 = proportion1
        self.proportion2 = proportion2
        if len(self.dataset) >= 2:
            return "Les données sont valides pour l'analyse."
        else:
            return "Le dataset doit contenir au moins deux observations pour le test de comparaison de deux proportions."
    
    def formHyp(self):
        return "H0: Les proportions des deux populations sont égales.\nH1: Les proportions des deux populations sont différentes."
        
    def distribution(self):
        return "Pas besoin d'analyser la distribution des données pour le test de comparaison de deux proportions."
        
    def testval(self):
        count = np.array([self.dataset.count(self.proportion1), self.dataset.count(self.proportion2)])
        nobs = np.array([len(self.dataset)] * 2)
        self.result=proportions_ztest(count, nobs)
        return str(proportions_ztest(count, nobs))
    
    def steps(self, alpha):
        self.alpha = float(alpha)
        return self.formHyp()
        
    def conclusion(self, alpha=0.05, desc=""):
        alpha=float(alpha)
        result = self.result
        p_value = result[1]
        if p_value < alpha:
            return "Il y a une différence significative entre les proportions des deux populations."
        else:
            return "Il n'y a pas de preuve statistique de différence significative entre les proportions des deux populations."
    
    def dataEntry(self):
        # Retourner les widgets utilisés pour entrer les données si nécessaire
        pass
    
    # Fonctions personnelles (optionnelles)
    def myFunction(self, myArg1, myArg2):
        # Méthode personnelle si nécessaire
        pass

if __name__ == "__main__":
    # Exemple d'utilisation de la classe TwoProportionsTest
    dataset = [[1, 1, 1, 0, 0, 0, 0, 0]]
    proportion1 = 1
    proportion2 = 0

    # Création d'une instance de TwoProportionsTest
    test = TwoProportionsTest(dataset)

    # Appel des méthodes pour tester la classe
    print("Contrôle des données:", test.datacontroller(proportion1, proportion2))
    print("Hypothèses formulées:", test.steps(0.05))
    print("Résultats du test de comparaison de deux proportions:")
    print("Résultat du test de comparaison de deux proportions:", test.testval())
    print("Conclusion:", test.conclusion())
