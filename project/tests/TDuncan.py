from scikit_posthocs import posthoc_dunn
import pandas as pd

class DuncanTest:
    def __init__(self, *data_groups):
        self.data_groups = data_groups

    def datacontroller(self):
        # Check if all data groups have the same length
        group_lengths = [len(group) for group in self.data_groups]
        if len(set(group_lengths)) > 1:
            raise ValueError("All data groups must have the same length.")

        # Combine all data groups into one DataFrame
        self.data = pd.concat(self.data_groups)

    def formHypotheses(self):
        return "H0: Les moyennes des groupes sont égales\nH1: Au moins une des moyennes des groupes est différente"

    def calculate_group_means(self):
        group_means = self.data.groupby('group')['vals'].mean().to_dict()
        return group_means

    def testval(self):
        return posthoc_dunn(self.data, group_col='group', val_col='vals')

    def steps(self):        
        group_means = self.calculate_group_means()
        results = self.testval()

        output = "Résultats du test de comparaisons multiples de Duncan :\n"
       
        output += "\n\nMoyennes des groupes d'échantillons :\n"
        for group, mean in group_means.items():
            output += f"{group}: {mean}\n"       
        output += str(results)

        return output

    def conclude(self):
        results = self.testval()
        conclusion = ""
        if results.min().min() < 0.05:
            conclusion = "Au moins une paire de moyennes des groupes est différente"
        else:
            conclusion = "Il n’existe pas suffisamment de preuves pour conclure que les moyennes de tous les groupes sont différentes."
        
        return conclusion

# Exemple d'utilisation
if __name__ == '__main__':
    data1 = pd.DataFrame({'group': 'A', 'vals': [5, 4, 8, 6, 3]})
    data2 = pd.DataFrame({'group': 'B', 'vals': [9, 7, 8, 6, 9]})
    data3 = pd.DataFrame({'group': 'C', 'vals': [3, 5, 2, 3, 7]})
    data4 = pd.DataFrame({'group': 'D', 'vals': [2, 3, 4, 1, 4]})
    data5 = pd.DataFrame({'group': 'E', 'vals': [7, 6, 9, 4, 7]})


# duncan_test = TDuncan(data1, data2, data3, data4, data5)
# print(duncan_test.formHypotheses())  # Print the null and alternative hypotheses
# duncan_results = duncan_test.steps()  
# print(duncan_results)  # Print detailed steps and results
# duncan_test.conclude()  # Print a final conclusion
