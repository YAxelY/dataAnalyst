from scipy.stats import wilcoxon

class WilcoxonTest:
    def init(self, dataSet):
        self.data1, self.data2 = dataSet  # Séparation du tuple en deux ensembles de données distincts

    def datacontroller(self):
        """ Exécute le test de Wilcoxon sur les échantillons appariés. """
        self.stat, self.p_value = wilcoxon(self.data1, self.data2)

    def formHyp(self):
        """ Formule les hypothèses nulle et alternative. """
        return ("H0 : Il n'y a pas de différence significative entre les deux échantillons.\n"
                "H1 : Il y a une différence significative entre les deux échantillons.")

    def distribution(self):
        """ Décrit la distribution utilisée pour le test. """
        return "Le test de Wilcoxon est utilisé."

    def testval(self):
        """ Renvoie la p-value du test. """
        return f"p-value : {self.p_value:.4f}"

    def steps(self):
        """ Fournit des résultats détaillés du test, incluant la statistique. """
        return (f"Statistique : {self.stat:.4f}\n"
                f"p-value : {self.p_value:.4f}")

    def conclusion(self, alpha=0.05):
        """ Détermine si l'hypothèse nulle peut être rejetée. """
        alpha = float(alpha)
        if self.p_value < alpha:
            return "L'hypothèse nulle (H0) est rejetée. Il y a une différence significative entre les échantillons."
        else:
            return "Il n'y a pas suffisamment de preuves pour rejeter l'hypothèse nulle (H0)."

# Utilisation de l'instance de la classe WilcoxonTest
dataSet = ([9, 10, 11, 10, 14, 15, 18, 10, 14, 12], [8, 10, 12, 9, 17, 13, 15, 11, 14, 10])
test = WilcoxonTest(dataSet)
test.datacontroller()
print(test.formHyp())
print(test.distribution())
print(test.testval())
print(test.steps())
print(test.conclusion())