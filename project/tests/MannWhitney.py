from scipy.stats import mannwhitneyu

class MannWhitney:
    def __init__(self, data1, data2,type="two-sided"):
        self.data1 = data1
        self.data2 = data2
    
    def formHyp(self):
        
        
        return "H_0: U_A = U_B \n H_1: U_A = U_B"
    
    def distribution(self):
        # Add your Mann-Whitney U test p-value calculation here

       pass
    

    def testval(self):
        
        result = mannwhitneyu(self.data1, self.data2)
        return result
    

    
    def steps(self):

        result=self.testval()
        # Calculate sum of ranks for group A
        n_1 = len(self.data1)
        sum_ranks_1 = result[0] - (n_1 * (n_1 + 1)) / 2

        # Calculate sum of ranks for group B
        n_2 = len(self.data2)
        sum_ranks_2 = (n_1 * n_2) - sum_ranks_1

        # Print the sum of ranks and U statistic
        print("Sum of ranks for group 1:", sum_ranks_1)
        print("Sum of ranks for group 2:", sum_ranks_2)
        print("U statistic:", result[0])

if __name__ == '__main__':
    data1 = [5, 7, 3, 8, 6]
    data2 = [10, 12, 9, 11, 13]
    mw = MannWhitney(data1, data2)
    mw.steps()

    data1 = [2.1, 4.0,5.4, 6.3, 8, 6]
    data2 = [10, 12, 9, 11, 13]
    mw1 = MannWhitney(data2, data1)
    mw1.steps()
            
            
  