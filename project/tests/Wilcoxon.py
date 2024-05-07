from scipy.stats import wilcoxon

class WilcoxonTest:
    def __init__(self, dataSet, test_type="two-sided"):
        self.data1, self.data2 = dataSet  # Séparation du tuple en deux ensembles de données distincts
        self.test_type = test_type
        if len(dataSet) != 2 or len(dataSet[0]) != len(dataSet[1]):
            raise ValueError("Les données doivent être un tuple de deux listes de longueur égale.")
                
            
        self.result = wilcoxon(self.data1, self.data2, alternative=self.test_type)
        self.stat = self.result.statistic
        self.p_value = self.result.pvalue

    def formHyp(self):
        """Formule les hypothèses nulle et alternative en fonction du type de test."""
        if self.test_type == "two-sided":
            return "H0 : Il n'y a pas de différence significative entre les deux échantillons.\n" \
                "H1 : Il y a une différence significative entre les deux échantillons."
        elif self.test_type == "greater":
            return "H0 : Le premier échantillon n'est pas significativement plus grand que le second.\n" \
                "H1 : Le premier échantillon est significativement plus grand que le second."
        elif self.test_type == "less":
            return "H0 : Le premier échantillon n'est pas significativement moins grand que le second.\n" \
                "H1 : Le premier échantillon est significativement moins grand que le second."

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

    def conclusion(self, alpha=0.05):
        """Détermine si l'hypothèse nulle peut être rejetée en fonction du niveau alpha."""
        alpha = float(alpha)
        if self.p_value < alpha:
            return f"Comme la p-value ({self.p_value:.4f}) est inférieure à alpha ({alpha}), nous rejetons l'hypothèse nulle."
        else:
            return f"Comme la p-value ({self.p_value:.4f}) est supérieure à alpha ({alpha}), nous ne rejetons pas l'hypothèse nulle."


    # def N(self):
    #         N=0
    #         for i in self.dataSet:
    #             N+=len(i)
# Exemple d'utilisation de la classe WilcoxonTest
