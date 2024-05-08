import numpy as np

class Duncan:
    def __init__(self, *data_set):
        self.data = data_set 

    def formHypotheses(self):
        return "H0: Les moyennes des groupes sont égales\nH1: Au moins une des moyennes des groupes est différente"

    def distribution(self):
       return "Test de Duncan"

    def testval(self):
        return 0

    def steps(self):
        groups = []
        for i, data_set in enumerate(self.data):
            values = [float(entry) for entry in data_set]
            group_mean = np.mean(values)
            groups.append((i+1, group_mean))

        ranked_groups = sorted(groups, key=lambda x: x[1])

        results = "Classement des groupes selon le test des multiples rangs de Duncan :\n"
        for rank, (group, mean) in enumerate(ranked_groups, start=1):
            results += f"- Rang {rank}: Groupe {group} (Moyenne: {round(mean, 4)})\n"
        
        return results

    def conclusion(self):   
        groups = []
        for i, data_set in enumerate(self.data):
            values = [float(entry) for entry in data_set]
            group_mean = np.mean(values)
            groups.append((i+1, group_mean))

        ranked_groups = sorted(groups, key=lambda x: x[1])
        
        differences = [ranked_groups[i+1][1] - ranked_groups[i][1] for i in range(len(ranked_groups)-1)]
        results = "\nDifférence entre les moyennes de chaque groupe :\n"
        for i, diff in enumerate(differences):
            results += f"- Différence entre le groupe {ranked_groups[i][0]} et le groupe {ranked_groups[i+1][0]} : {round(diff, 4)}\n"

        return results


if __name__ == '__main__':
    pass



# Example usage with multiple data groups
data1 = [5, 4, 8, 6, 3]
data2 = [9, 7, 8, 6, 9]
data3 = [3, 5, 2, 3, 7]
data4 = [2, 3, 4, 1, 4]
data5 = [7, 6, 9, 4, 7]


duncan_test = TDuncan(data1, data2, data3, data4, data5)
print(duncan_test.formHypotheses())  # Print the null and alternative hypotheses
duncan_steps = duncan_test.steps()  
print(duncan_steps)  # Print detailed steps
duncan_results = duncan_test.conclusion()  
print(duncan_results)  # Print detailed results
