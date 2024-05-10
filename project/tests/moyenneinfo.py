
import numpy as np
from scipy.stats import ttest_1samp, t
from scipy import stats
import scipy.stats

class OneSampleMeanTestGinfo:
    def __init__(self,data):
        self.data = data
    def datacontroller(self,theoretical_mean=0):
        



       
        self.n =float( self.data[0])
        self.mu_0 = float(self.data[3])
        self.sigma = float(self.data[1])
        self.X_bar = float( self.data[2])
        self.alpha = float(self.data[4])
        self.nature=self.data[5]
    

    def formHyp(self):
        hypothese_nulle = 'La moyenne de la population est egale à la moyenne theorique'
        hypothese_alternative = 'La moyenne de la population est differente de la moyenne theorique'
        return f'H0: {hypothese_nulle}\nH1: {hypothese_alternative}'
    def steps(self):
        pass

 
if  __name__== "__main__":
    data=["12","02","6","4","32"]
    new=OneSampleMeanTestGinfo(data)
    new.datacontroller()
    print(new.formHyp())

