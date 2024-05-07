from scipy.stats import f_oneway

class AnovaTwo:
    def __init__(self, data_set, mode="two sided"):
        self.data_set = data_set

    def form_hyp(self):
        n = len(self.data_set)
        symbol = "θ²"
        hypothesis_string = "H0: "
        for i in range(1, n + 1):
            if i > 1:
                hypothesis_string += "="
            hypothesis_string += symbol + "_{}".format(i)
        return hypothesis_string + "\nH_1: Au moins une moyenne diffère des autres"

    def distribution(self):
        print("On utilise la loi de Fisher")

    def testval(self):
        result = f_oneway(*self.data_set)
        return result

    def steps(self):
        f_statistic, p_value = self.testval()
        print("F-statistic:", f_statistic)
        print("p-value:", p_value)

    def conclusion(self, alpha=0.05):
        _, p_value = self.testval()
        if p_value < alpha:
            print("Rejet de l'hypothèse nulle")
        else:
            print("Échec de rejeter l'hypothèse nulle")

    def N(self):
        N = 0
        for i in self.data_set:
            N += len(i)

# Exemple d'utilisation
data_set = [
    [1, 2, 3],
    [2, 3, 4]
]

anova = AnovaTwo(data_set)
print(anova.form_hyp())
anova.distribution()
anova.steps()
anova.conclusion()
