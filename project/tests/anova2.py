import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

class AnovaTwo:
    def __init__(self, dataSet, mode="two sided"):
        self.dataSet = dataSet
        self.n = len(dataSet)
        
    # Common Interfaces
    def formHyp(self):
        symbol = "θ²"
        hypothesis_string = "H0: "
        for i in range(1, self.n + 1):
            if i > 1:
                hypothesis_string += "="
            hypothesis_string += symbol + "_{}".format(i)
        return hypothesis_string + "\nH_1: At least one mean differs from the others"
    
    def distribution(self):
        print("Using the Fisher distribution")
    
    def testval(self):
        df = pd.DataFrame(self.dataSet, columns=['water', 'sun', 'height'])
        model = ols('height ~ C(water) + C(sun) + C(water):C(sun)', data=df).fit()
        anova_table = sm.stats.anova_lm(model, type=2)
        return anova_table

    def steps(self):
        anova_table = self.testval()
        print("ANOVA Table:")
        print(anova_table)

    def conclusion(self, alpha=0.05):
        anova_table = self.testval()
        p_value_interaction = anova_table.loc['C(water):C(sun)', 'PR(>F)']
        if p_value_interaction < alpha:
            print("-----------------------------------------------------------------------------\n")
            print("The interaction between the factors water and sun is significant.")
        else:
            print("----------------------------------------------------------------")
            print("The interaction between the factors water and sun is not significant.")
        p_values_main_effects = anova_table.loc[['C(water)', 'C(sun)'], 'PR(>F)']
        for factor, p_value in p_values_main_effects.items():
            if p_value < alpha:
                print("--------------------------------")
                print(f"The effect of the factor {factor} is significant.")
            else:
                print("--------------------------------")
                print(f"The effect of the factor {factor} is not significant.")

# Creating the data
data = {'water': np.repeat(['daily', 'weekly'], 15),
        'sun': np.tile(np.repeat(['low', 'med', 'high'], 5), 2),
        'height': [6, 6, 6, 5, 6, 5, 5, 6, 4, 5,
                    6, 6, 7, 8, 7, 3, 4, 4, 4, 5,
                    4, 4, 4, 4, 4, 5, 6, 6, 7, 8]}

# Instantiating the AnovaTwo class
anova = AnovaTwo(data)

# Using the class methods
print(anova.formHyp())
anova.distribution()
anova.steps()
anova.conclusion()
