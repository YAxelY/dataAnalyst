from scipy.stats import mannwhitneyu

class MannWhitne:
    def __init__(self, data1, data2,type="one-way"):
        self.data1 = data1
        self.data2 = data2
    
    def formHyp(self):
        
        
        return "H_0: U_1 = U_2 \n H_1: U_1 = U_2"
    
    def distribution(self):
        # Add your Mann-Whitney U test p-value calculation here

       pass
    

    def testval(self):
        
        result = mannwhitneyu(self.data1, self.data2)
        return result
    

    
    def steps(self):

        u1,p_value = self.testval()
        # Calculate sum of ranks for group A
        n_1 = len(self.data1)
        sum_ranks_1 = u1 + (n_1 * (n_1 + 1)) / 2


        # Calculate sum of ranks for group B
        n_2 = len(self.data2)
        u2=n_1*n_2-u1
        sum_ranks_2 = u2 + (n_2 * (n_2 + 1)) / 2

        # Print the sum of ranks and U statistic
        print("Sum of ranks for group 1:", sum_ranks_1)
        print("U_1:", u1)
        print("Sum of ranks for group 2:", sum_ranks_2)
        print("U_2", u2)
        print("p-value:", p_value )

    def conclusion(self,alpha = 0.05):

        _ , p_value = self.testval()
        if p_value < alpha:
            print("Reject the null hypothesis")
        else:
            print("Fail to reject the null hypothesis")

       


if __name__ == '__main__':
    pass