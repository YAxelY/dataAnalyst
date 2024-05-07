from scipy.stats import mannwhitneyu # type: ignore

class AnovaOne:
    def __init__(self, dataSet,mode="two sided"):
        self.dataSet = dataSet
        n = len(dataSet)

        
    #commun interfaces
    def formHyp(self):

        n=len(self.dataSet)
        symbol = "θ²"
        hypothesis_string = "H0: "
        for i in range(1, n+ 1):
            if i > 1:
                hypothesis_string += "="
            hypothesis_string += symbol + "_{}".format(i)

      


        
        
        return hypothesis_string+ "\nH_1: Au moins une moyenne diffère des autres"
    
    def distribution(self):
        

       print("on utise la loi de Fisher au ddl")
    

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
    
    #personnal function
    def N(self):
        N=0
        for i in self.dataSet:
            N+=len(i)


    

       


if __name__ == '__main__':
    pass