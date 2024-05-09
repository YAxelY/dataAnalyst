from scipy.stats import wilcoxon

<<<<<<< HEAD
class WilcoxonTest:
    def __init__(self, dataSet, test_type="two-sided"):
        self.data1, self.data2 = dataSet  # Séparation du tuple en deux ensembles de données distincts
        self.test_type = test_type
        if len(dataSet) != 2 or len(dataSet[0]) != len(dataSet[1]):
            raise ValueError("Les données doivent être un tuple de deux listes de longueur égale.")
                
            
# =======
class Wilcoxon:
    def __init__(self, dataSet):
      self.data=dataSet

    def datacontroller(self,test_type="two-sided"):
        dataSet=self.data
        self.test_type=test_type
        if len(dataSet) != 2 or len(dataSet[0]) != len(dataSet[1]):
            raise ValueError("Les données doivent être un tuple de deux listes de longueur égale.")
        self.data1, self.data2 = dataSet  # Séparation du tuple en deux ensembles de données distincts
        self.test_type = test_type
# >>>>>>> 228a0535364e44925f000f0c17fab78e22bc51d7
        self.result = wilcoxon(self.data1, self.data2, alternative=self.test_type)
        self.stat = self.result.statistic
        self.p_value = self.result.pvalue

    def formHyp(self):
        """Formule les hypothèses nulle et alternative en fonction du type de test."""
        if self.test_type == "two-sided":
            return "H0 : Il n'y a pas de différence significative entre les deux échantillons.\n" \
<<<<<<< HEAD
                "H1 : Il y a une différence significative entre les deux échantillons."
        elif self.test_type == "greater":
            return "H0 : Le premier échantillon n'est pas significativement plus grand que le second.\n" \
                "H1 : Le premier échantillon est significativement plus grand que le second."
        elif self.test_type == "less":
            return "H0 : Le premier échantillon n'est pas significativement moins grand que le second.\n" \
                "H1 : Le premier échantillon est significativement moins grand que le second."
=======
                   "H1 : Il y a une différence significative entre les deux échantillons."
        elif self.test_type == "greater":
            return "H0 : Le premier échantillon n'est pas significativement plus grand que le second.\n" \
                   "H1 : Le premier échantillon est significativement plus grand que le second."
        elif self.test_type == "less":
            return "H0 : Le premier échantillon n'est pas significativement moins grand que le second.\n" \
                   "H1 : Le premier échantillon est significativement moins grand que le second."
>>>>>>> 228a0535364e44925f000f0c17fab78e22bc51d7

    def distribution(self):
        """Décrit la distribution utilisée pour le test."""
        return "Le test de rang signé de Wilcoxon est utilisé, un test non paramétrique pour comparer deux échantillons appariés."

    def testval(self):
        """Renvoie la p-value du test."""
        return f"p-value : {self.p_value:.4f}"

    def steps(self, alpha=0.05):
        """Fournit des résultats détaillés du test, y compris la statistique et la p-value, avec une interprétation basée sur alpha."""
        alpha = float(alpha)
        réponse = f"Statistique : {self.stat}\n"
        réponse += f"p-value : {self.p_value:.4f}\n"
        if self.p_value < alpha:
            réponse += "Rejet de l'hypothèse nulle : Il y a une différence significative."
        else:
            réponse += "Non-rejet de l'hypothèse nulle : Aucune différence significative."
        return réponse

<<<<<<< HEAD
    def conclusion(self, alpha=0.05):
=======
    def conclusion(self, alpha=0.05,desc=""):
>>>>>>> 228a0535364e44925f000f0c17fab78e22bc51d7
        """Détermine si l'hypothèse nulle peut être rejetée en fonction du niveau alpha."""
        alpha = float(alpha)
        if self.p_value < alpha:
            return f"Comme la p-value ({self.p_value:.4f}) est inférieure à alpha ({alpha}), nous rejetons l'hypothèse nulle."
        else:
            return f"Comme la p-value ({self.p_value:.4f}) est supérieure à alpha ({alpha}), nous ne rejetons pas l'hypothèse nulle."


<<<<<<< HEAD
    # def N(self):
    #         N=0
    #         for i in self.dataSet:
    #             N+=len(i)
# Exemple d'utilisation de la classe WilcoxonTest
=======
if __name__=="__main__":
    # Exemple d'utilisation de la classe WilcoxonTest
    dataSet = ([9, 10, 11, 10, 14, 15, 18, 10, 14, 12], [8, 10, 12, 9, 17, 13, 15, 11, 14, 10])
    test = Wilcoxon(dataSet)

    
    print(test.datacontroller())
    print(test.formHyp())

    print(test.distribution())
    print(test.testval())
    print(test.steps())
    print(test.conclusion())
>>>>>>> 228a0535364e44925f000f0c17fab78e22bc51d7
