import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the module from the parent package
import Style as st

from scipy.stats import mannwhitneyu  # type: ignore



class MannWhitney:

    # définition commune à toutes les classes
    def __init__(self,dataSet,type="two-sided"):
        self.data = dataSet
        self.dataEntry = 0   # set to 1 if you did implement
        
    
    def formHyp(self):
      
        
        return "<red H_0:>U_1 = U_2 \nH_1: U_1 = U_2"

    def datacontroller(self):
        if True :
            self.data1 = self.data[0]
            self.data2 = self.data[1]
            self.result = mannwhitneyu(self.data1, self.data2)
            

    
    def distribution(self):
        # Add your Mann-Whitney U test p-value calculation here

       return "comme on compare 2 moyennes sans aucunes informations de normalité sur les données\n on utilise le test de Mann Whitney car test non paramétrique" 
    

    def testval(self):
        
       
        
        return "p-value: "+ str(self.result[1])
    

    
    def steps(self,alpha=0.05):
        alpha = float(alpha)

        u1,p_value = mannwhitneyu(self.data1, self.data2)
        # Calculate sum of ranks for group A
        n_1 = len(self.data1)
        sum_ranks_1 = u1 + (n_1 * (n_1 + 1)) / 2


        # Calculate sum of ranks for group B
        n_2 = len(self.data2)
        u2=n_1*n_2-u1
        sum_ranks_2 = u2 + (n_2 * (n_2 + 1)) / 2

        # # Print the sum of ranks and U statistic
        # print("Sum of ranks for group 1:", sum_ranks_1)
        # print("U_1:", u1)
        # print("Sum of ranks for group 2:", sum_ranks_2)
        # print("U_2", u2)
        # print("p-value:", p_value )
        pR1= "sum of ranks for group 1 "+str(sum_ranks_1)+"\n"
        pu1= "U1: "+str(u1)+"\n"
        pR2="sum of ranksfor group 2" +str(sum_ranks_2)+"\n"
        pu2= "U2: "+str(u2)+"\n"
        pv="<red p-value: >"+""+str(p_value)+"\n"
        string= pR1+pu1+pR2+pu2+pv
        

        return string


    def conclusion(self,alpha = 0.05,desc=""):
        if desc!="":
            desc="("+desc+")"

        _ , p_value = self.result
        alpha = float(alpha)
        desc= str(desc)
        if p_value < alpha:
            dec= "comme "+str(p_value)+"< "+str(alpha)+", H0 est rejetée"+"\n"
            con= "Au risque de se tromper de "+str(alpha)+"%.on peut conclure que l'hypothèse null "+desc+" est fausse"
            # print("Reject the null hypothesis")
            return dec+con
        else:
            dec= "comme "+str(p_value)+"> "+str(alpha)+", H0 est accepté"+"\n"
            con= "Au risque de se tromper de "+str(alpha)+"%.On peut conclure que l'hypothèse null "+desc+" est vraie"
            return dec+con
    
    # definition optionnelle

    def dataEntry(self):
        pass

    # fonctions personnelles à la classe

    def myfunction1(self):
        pass

       


if __name__ == '__main__':

    data1 = [5, 7, 3, 8, 6]
    data2 = [10, 12, 9, 11, 13]
    mw = MannWhitney(data1, data2)
    mw.steps()

    data1 = [2.1, 4.0,5.4, 6.3, 8, 6]
    data2 = [10, 12, 9, 11, 13]
    mw1 = MannWhitney(data2, data1)
    mw1.steps()
            
            
  