from scipy.stats import f_oneway
from scipy.stats import f
from prettytable import PrettyTable
from tkinter import messagebox
class AnovaTwoWayR:
    def __init__(self, data_set):
        self.data = data_set
        
    def datacontroller(self):
        
        self.data = [sublist for sublist in self.data if sublist]
        print(self.data)
        
        self.tj=self.compute_sum_of_tj( self.data)
        
        self.ti=self.compute_sum_of_ti( self.data)
        
        self.T_2=self.compute_sum_of_tr( self.data)
      
        self.c=len( self.data[0])
       
        self.r=len( self.data)
       
        self.n=len(self.data[0][0])
      
       
        self.cf=(self.T_2*self.T_2)/(self.c*self.r*self.n)
        self.sst=self.compute_sum_of_squares_in_array_of_arrays( self.data)-self.cf
       
        self.ssc=self.compute_sum_of_squares_in_array(self.tj)/(self.r*self.n)-self.cf
      
        self.ssr=self.compute_sum_of_squares_in_array(self.ti)/(self.c*self.n)-self.cf
        
        self.ssrc=self.compute_sum_of_squares_for_sscr( self.data)/self.n-self.ssr-self.ssc-self.cf
       
        self.sse=self.sst-self.ssc-self.ssr-self.ssrc

        
       
        self.ddlc=self.c-1
        self.ddlr=self.r-1
        self.ddlrc=self.ddlc*self.ddlr
        self.ddle=self.c*self.r*(self.n-1)
        self.ddlt=self.c*self.r*self.n-1
        self.msc=self.ssc/self.ddlc
        self.msr=self.ssr/self.ddlr
        self.msrc=self.ssrc/self.ddlrc
        self.mse=self.sse/self.ddle
        self.fc=self.msc/self.mse
        self.fr=self.msr/self.mse
        self.frc=self.msrc/self.mse
        
        

            
            
    def formHyp(self):
        # Constructing the null and alternative hypotheses
        symbol_alpha = "α"
        symbol_beta = "β"
        hypothesis_string = ""
        
        # Null hypothesis H0
        hypothesis_string += f"{symbol_alpha}_i est l'effet sur les lignes\n"
        hypothesis_string += f"{symbol_beta}_j est l'effet sur les colonnes\n"
      
        hypothesis_string += "H0: "
        for i in range(1, self.r+1):
            if i > 1:
                hypothesis_string += " = "
            hypothesis_string += symbol_alpha + "_{}".format(i)
        hypothesis_string += "\nH0': "
        for j in range(1, self.c+1):
            if j > 1:
                hypothesis_string += " = "
            hypothesis_string += symbol_beta + "_{}".format(j)
        hypothesis_string += "\nH0'': "
        for j in range(1, self.c+1):
            if j > 1:
                hypothesis_string += " = "
            
            for i in range(1, self.c+1):
                if i > 1:
                    hypothesis_string += " = "
                hypothesis_string += "("+symbol_alpha+symbol_beta +")"+ "_{}".format(j)+"{}".format(i)
    
        # Alternative hypothesis H1
        hypothesis_string += "\nH1: Au moins une des moyennes sur les lignes diffère des autres"
        
        # Additional alternative hypothesis considering the rows and columns effects
        hypothesis_string += "\nH1': Au moins une des moyennes sur les colonnes diffère des autres"
        # Additional alternative hypothesis considering the rows and columns effects
        hypothesis_string += "\nH1'': il existeau moins un (αβ)_ij qui diffère des autres"


        return hypothesis_string



    
    def distribution(self):
        return "On utilise la loi de Fisher (F-distribution) car ANOVA à deux facteurs avec replications"
    
    def steps(self, alpha):
        self.alpha=alpha
        return str(self.generate_pretty_table(self.ssc,self.ddlc,self.msc,self.fc,self.ssr,self.ddlr,self.msr,\
                                          self.fr,self.ssrc,self.ddlrc,self.msrc,self.frc,self.sse,self.ddle,self.mse,self.sst,self.ddlt))
    
    def testval(self):
        self.alpha=float(self.alpha)
        self.upper_bound_INRH0 = f.ppf(1 - self.alpha, self.ddlr, self.ddle)
        self.upper_bound_INRH0_ = f.ppf(1 - self.alpha, self.ddlc, self.ddle)
        self.upper_bound_INRH0__=f.ppf(1-self.alpha,self.ddlrc,self.ddle)
        result = ""
        result += f"INRH0: [0, {self.upper_bound_INRH0}]\n"
        result += f"INRH0': [0, {self.upper_bound_INRH0_}]\n"
        result += f"INRH0'': [0, {self.upper_bound_INRH0__}]"
        return result



        
    def conclusion(self, alpha=0.05, desc=""):
            alpha = float(alpha)
            if self.fc > self.upper_bound_INRH0 and self.fr > self.upper_bound_INRH0_ and self.frc > self.upper_bound_INRH0__:
                return f"Nous rejetons l'hypothèse nulle (H0), l'hypothèse nulle (H0') et l'hypothèse nulle (H0''). Au risque de se tromper de {alpha*100}%, Il y a une différence significative entre les moyennes des groupes pour les effets sur les lignes, sur les colonnes et sur leur interaction."
            elif self.fc > self.upper_bound_INRH0 and self.fr > self.upper_bound_INRH0_:
                return f"Nous rejetons l'hypothèse nulle (H0) et l'hypothèse nulle (H0') pour les effets sur les lignes et sur les colonnes respectivement. Cependant, nous acceptons l'hypothèse nulle (H0'') pour l'interaction des lignes et des colonnes. Au risque de se tromper de {alpha*100}%, Il y a une différence significative entre les moyennes des groupes pour les effets sur les lignes et sur les colonnes, mais pas pour leur interaction."
            elif self.fc > self.upper_bound_INRH0:
                return f"Nous rejetons l'hypothèse nulle (H0) pour les effets sur les lignes, mais nous acceptons l'hypothèse nulle (H0') pour les effets sur les colonnes et l'hypothèse nulle (H0'') pour leur interaction. Au risque de se tromper de {alpha*100}%, Il y a une différence significative entre les moyennes des groupes pour les effets sur les lignes."
            elif self.fr > self.upper_bound_INRH0_:
                return f"Nous acceptons l'hypothèse nulle (H0) pour les effets sur les lignes, mais nous rejetons l'hypothèse nulle (H0') pour les effets sur les colonnes et l'hypothèse nulle (H0'') pour leur interaction. Au risque de se tromper de {alpha*100}%, Il y a une différence significative entre les moyennes des groupes pour les effets sur les colonnes."
            elif self.frc > self.upper_bound_INRH0__:
                return f"Nous acceptons l'hypothèse nulle (H0) pour les effets sur les lignes et sur les colonnes, mais nous rejetons l'hypothèse nulle (H0'') pour leur interaction. Au risque de se tromper de {alpha*100}%, Il y a une différence significative entre les moyennes des groupes pour l'interaction des lignes et des colonnes."
            else:
                return f"Nous acceptons l'hypothèse nulle (H0), l'hypothèse nulle (H0') et l'hypothèse nulle (H0''). Au risque de se tromper de {alpha*100}%, Les moyennes des groupes sont statistiquement similaires pour les effets sur les lignes, sur les colonnes et pour leur interaction."

    def dataEntry(self):
        # Implement data entry GUI components here
        pass
    
    def my_function(self, my_arg1, my_arg2):
        # Implement your custom function logic here
        pass



    def compute_sum_of_tr(self,arrays):
        total_sum = 0
        for array in arrays:
            for item in array:
                for i in item:
                    total_sum += i
        return total_sum


    def compute_sum_of_ti(self, arrays):
        sum_of_ti = [0] * len(arrays)
        for i, array in enumerate(arrays):
            sum_of_ti[i] = sum([item for sublist in array for item in sublist])
        return sum_of_ti


    def compute_sum_of_tj(self,arrays):
        if not arrays:
            return []

        max_length = max(len(array) for array in arrays)
        sum_of_tj = [0] * max_length
        
        for array in arrays:
            for index, item in enumerate(array):
                sum_of_tj[index] += sum(item)
        
        return sum_of_tj

    def compute_sum_of_squares_in_array_of_arrays(self,arrays):
        total_sum_of_squares = 0
        for array in arrays:
            for item in array:
                for i in item:
                    total_sum_of_squares += i ** 2
        return total_sum_of_squares
    
    def compute_sum_of_squares_for_sscr(self,arrays):
        total_sum_of_squares = 0
        for array in arrays:
            for item in array:
               
                total_sum_of_squares += sum(item)*sum(item)
        return total_sum_of_squares


    def compute_sum_of_squares_in_array(self,array):
        return sum(item ** 2 for item in array)

    def generate_pretty_table(self,ssc, c_minus_1, msc, fc, ssr, r_minus_1, msr, fr,ssrc,ddlrc,msrc,frc, sse, ddle, mse, sst, cr_minus_2):
        table = PrettyTable(["source de variation", "sommes des carrés", "dégré de liberté", "carrées des moyennes", "valeur du test"])
        table.add_row(["effet sur les colonnes", ssc, c_minus_1, msc, fc])
        table.add_row(["effet sur les lignes", ssr, r_minus_1, msr, fr])
        table.add_row(["Inter-action", ssrc, ddlrc, msrc, frc])
        table.add_row(["erreur", sse, ddle, mse, "NaN"])
        table.add_row(["total", sst, cr_minus_2, "NaN", "NaN"])
        return table

# # Example usage
# ssc = 10
# c_minus_1 = 3
# msc = 3.33
# fc = 1.5
# ssr = 20
# r_minus_1 = 4
# msr = 5
# fr = 2.5
# sse = 15
# cr_minus_1 = 11
# mse = 1.36
# sst = 45
# cr_minus_1 = 11

# pretty_table = generate_pretty_table(ssc, c_minus_1, msc, fc, ssr, r_minus_1, msr, fr, sse, cr_minus_1, mse, sst, cr_minus_1)
# print(pretty_table)

if __name__=="__main__":     
    A1=[64,66,70]
    A2=[72,81,64]
    A3=[74,51,65]
    B1=[65,63,58]
    B2=[57,43,52]
    B3=[47,58,67]
    C1=[59,68,65]
    C2=[66,71,59]
    C3=[58,39,42]
    D1=[58,41,46]
    D2=[57,61,53]
    D3=[53,59,38]

    array=[[A1,A2,A3],[B1,B2,B3],[C1,C2,C3],[D1,D2,D3]]        
   
    ano=AnovaTwoWayR(array)
    ano.datacontroller()
    print(ano.formHyp())
    print(ano.distribution())
    print(ano.steps(0.05))
    print(ano.testval())
    
    print(ano.conclusion())