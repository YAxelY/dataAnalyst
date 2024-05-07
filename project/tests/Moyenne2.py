import numpy as np
from scipy.stats import norm

class OneSampleMeanTestG:
    def __init__(self,data):
        self.data = data

       
       
    def datacontroller(self,theoretical_mean=0):
        self.data = [sublist for sublist in self.data if sublist]
    
        self.theoretical_mean=theoretical_mean
     
       
        if len(self.data)>=2:
            print("ok")  
    def formHyp(self,theoretical_mean=0.05):
        
        hypothesis_string = f'H0: μ = {self.theoretical_mean}\n'
        hypothesis_string += 'H1: μ ≠ {}'.format(self.theoretical_mean)
        return hypothesis_string
    
    def distribution(self):
        if len(self.data) >= 30:
            return "We use the normal distribution"
        else:
            return "We use the t-distribution"
    
    def testval(self):
        z_value = (np.mean(self.data) - self.theoretical_mean) / (np.std(self.data) / np.sqrt(len(self.data)))
        p_value = 2 * (1 - norm.cdf(abs(z_value)))  # Two-tailed test
        return f"Test statistic (z-value): {z_value:.4f}\np-value: {p_value:.4f}"
    
    def steps(self, alpha):
        alpha = float(alpha)
        return f'Critical values for the normal distribution are not applicable. Use z-table or software for calculation.'
    
    def conclusion(self, alpha=0.05,desc=""):
        alpha = float(alpha)
        z_value = (np.mean(self.data) - self.theoretical_mean) / (np.std(self.data) / np.sqrt(len(self.data)))
        p_value = 2 * (1 - norm.cdf(abs(z_value)))  # Two-tailed test
            
        if p_value < alpha:
            return "We reject the null hypothesis (H0). There is a significant difference between the sample mean and the theoretical mean."
        else:
            return "We fail to reject the null hypothesis (H0). The sample mean is not significantly different from the theoretical mean."

if __name__=="__main__":
    data=[[12,15,9,45]]
    t=OneSampleMeanTestG(data,0.05)
    t.datacontroller()
    t.formHyp()
    t.steps(0.05)
    t.conclusion()