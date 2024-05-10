import numpy as np
from statsmodels.stats.proportion import proportions_ztest

class ProportionToTheoreticalTest:
    def __init__(self, dataset):
        self.data = dataset
        self.dataset=self.data
       
        
    def datacontroller(self, theoretical_proportion=0):
        self.theoretical_proportion = theoretical_proportion
        self.dataset=self.data[0]
        print(self.theoretical_proportion)
        print(self.dataset)
        if len(self.dataset) >= 1:
            return "Les données sont valides pour l'analyse."
        else:
            return "Le dataset doit contenir au moins une observation pour le test de comparaison de proportion à une proportion théorique."
    
    def formHyp(self):
        return f"H0: La proportion de la population est égale à la proportion théorique {self.theoretical_proportion}.\nH1: La proportion de la population est différente de la proportion théorique."
        
    def distribution(self):
        return "Pas besoin d'analyser la distribution des données pour le test de comparaison de proportion à une proportion théorique."
        
    # def testval(self):
    #     count = self.dataset.count(1)
    #     nobs = len(self.dataset)
    #     self.testvalr=proportions_ztest(count, nobs, self.theoretical_proportion)
    #     return str(proportions_ztest(count, nobs, self.theoretical_proportion))
    def testval(self):
        count = self.dataset.count(1)
        nobs = len(self.dataset)
        self.result= proportions_ztest(count, nobs, self.theoretical_proportion)
        return f"Test de comparaison de proportions : {self.result}"


    
    def steps(self, alpha):
        self.alpha = float(alpha)
        return self.formHyp()
        
    def conclusion(self, alpha=0.05, desc=""):
        alpha=float(alpha)
        result = self.result
        p_value = result[1]
        if p_value < alpha:
            return f"Il y a une différence significative entre la proportion de la population et la proportion théorique {self.theoretical_proportion}."
        else:
            return f"Il n'y a pas de preuve statistique de différence significative entre la proportion de la population et la proportion théorique {self.theoretical_proportion}."
    
    def dataEntry(self):
        # Retourner les widgets utilisés pour entrer les données si nécessaire
        pass
    
    # Fonctions personnelles (optionnelles)
    def myFunction(self, myArg1, myArg2):
        # Méthode personnelle si nécessaire
        pass

if __name__ == "__main__":
    # Exemple d'utilisation de la classe ProportionToTheoreticalTest
    dataset = [[1, 1, 1, 0, 0, 0, 0, 0]]
    theoretical_proportion = 0.5

    # Création d'une instance de ProportionToTheoreticalTest
    test = ProportionToTheoreticalTest(dataset)

    # Appel des méthodes pour tester la classe
    print("Contrôle des données:", test.datacontroller(theoretical_proportion))
    print("Hypothèses formulées:", test.steps(0.05))
    print("Résultats du test de comparaison de la proportion à une proportion théorique:")
    print("Résultat du test de comparaison de la proportion à une proportion théorique:", test.testval())
    print("Conclusion:", test.conclusion())
