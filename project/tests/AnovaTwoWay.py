from scipy.stats import f_oneway
from scipy.stats import f
from prettytable import PrettyTable
from tkinter import messagebox
class AnovaTwoWay:
    def __init__(self, data_set):
        self.data = data_set
        
    def datacontroller(self):
        self.data = [sublist for sublist in self.data if sublist]
        
        
        self.tj=self.compute_sum_of_tj( self.data)
        self.ti=self.compute_sum_of_ti( self.data)
        self.T_2=self.compute_sum_of_t( self.data)
        self.c=len( self.data[0])
        self.r=len( self.data)
       
        self.cf=(self.T_2*self.T_2)/(self.c*self.r)
        self.sst=self.compute_sum_of_squares_in_array_of_arrays( self.data)-self.cf
        self.ssc=self.compute_sum_of_squares_in_array(self.tj)/self.r-self.cf
        self.ssr=self.compute_sum_of_squares_in_array(self.ti)/self.c-self.cf
        self.sse=self.sst-self.ssc-self.ssr
        self.ddlc=self.c-1
        self.ddlr=self.r-1
        self.ddle=self.ddlc*self.ddlr
        self.msc=self.ssc/self.ddlc
        self.msr=self.ssr/self.ddlr
        self.mse=self.sse/self.ddle
        self.fc=self.msc/self.mse
        self.fr=self.msr/self.mse
        
            
            
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
        
        # Alternative hypothesis H1
        hypothesis_string += "\nH1: Au moins une des moyennes sur les lignes diffère des autres"
        
        # Additional alternative hypothesis considering the rows and columns effects
        hypothesis_string += "\nH1': Au moins une des moyennes sur les colonnes diffère des autres"

        return hypothesis_string



    
    def distribution(self):
        return "On utilise la loi de Fisher (F-distribution) car ANOVA à deux facteurs sans replications"
    
    def steps(self, alpha):
        self.alpha=alpha
        return str(self.generate_pretty_table(self.ssc,self.c-1,self.msc,self.fc,self.ssr,self.r-1,self.msr,\
                                          self.fr,self.sse,(self.c-1)*(self.r-1),self.mse,self.sst,self.c*self.r-1))
    
    def testval(self):
        self.alpha=float(self.alpha)
        self.upper_bound_INRH0 = f.ppf(1 - self.alpha, self.ddlr, self.ddle)
        self.upper_bound_INRH0_ = f.ppf(1 - self.alpha, self.ddlc, self.ddle)
        result = ""
        result += f"INRH0: [0, {self.upper_bound_INRH0}]\n"
        result += f"INRH0': [0, {self.upper_bound_INRH0_}]"
        return result



        
    def conclusion(self, alpha=0.05,desc=""):
        alpha=float(alpha)
        if self.fc > self.upper_bound_INRH0 and self.fr > self.upper_bound_INRH0_:
            return f"Nous rejetons l'hypothèse nulle (H0) et l'hypothèse nulle (H0') pour les effets sur les lignes et sur les colonnes. Au risque de se tromper de {alpha*100}%, Il y a une différence significative entre les moyennes des groupes."
        elif self.fc > self.upper_bound_INRH0:
            return f"Nous rejetons l'hypothèse nulle (H0) pour les effets sur les lignes, mais nous acceptons l'hypothèse nulle (H0') pour les effets sur les colonnes. Au risque de se tromper de {alpha*100}%, Il y a une différence significative entre les moyennes des groupes pour les effets sur les lignes."
        elif self.fr > self.upper_bound_INRH0_:
            return f"Nous acceptons l'hypothèse nulle (H0) pour les effets sur les lignes, mais nous rejetons l'hypothèse nulle (H0') pour les effets sur les colonnes.  Au risque de se tromper de {alpha*100}%, Il y a une différence significative entre les moyennes des groupes pour les effets sur les colonnes."
        else:
            return f"Nous acceptons l'hypothèse nulle (H0) et l'hypothèse nulle (H0').Au risque de se tromper de {alpha*100}%, Les moyennes des groupes sont statistiquement similaires pour les effets sur les lignes et sur les colonnes. "

    def dataEntry(self):
        # Implement data entry GUI components here
        pass
    
    def my_function(self, my_arg1, my_arg2):
        # Implement your custom function logic here
        pass



    def compute_sum_of_t(self,arrays):
        total_sum = 0
        for array in arrays:
            for item in array:
                total_sum += item
        return total_sum


    def compute_sum_of_ti(self,arrays):
        sum_of_ti = []
        for array in arrays:
            sum_of_ti.append(sum(array))
        return sum_of_ti


    def compute_sum_of_tj(self,arrays):
        if not arrays:
            return []

        max_length = max(len(array) for array in arrays)
        sum_of_tj = [0] * max_length
        
        for array in arrays:
            for index, item in enumerate(array):
                sum_of_tj[index] += item
        
        return sum_of_tj

    def compute_sum_of_squares_in_array_of_arrays(self,arrays):
        total_sum_of_squares = 0
        for array in arrays:
            for item in array:
                total_sum_of_squares += item ** 2
        return total_sum_of_squares

    def compute_sum_of_squares_in_array(self,array):
        return sum(item ** 2 for item in array)

    def generate_pretty_table(self,ssc, c_minus_1, msc, fc, ssr, r_minus_1, msr, fr, sse, cr_minus_1, mse, sst, cr_minus_2):
        table = PrettyTable(["source de variation", "sommes des carrés", "dégré de liberté", "carrées des moyennes", "valeur du test"])
        table.add_row(["effet sur les colonnes", ssc, c_minus_1, msc, fc])
        table.add_row(["effet sur les lignes", ssr, r_minus_1, msr, fr])
        table.add_row(["erreur", sse, (c_minus_1)*(r_minus_1), mse, "NaN"])
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
    E1=[64,72,74]
    E2=[55,57,47]
    E3=[59,66,58]
    E4=[58,57,53]
    array=[E1,E2,E3,E4]        
    # print(compute_sum_of_t(array))
    # print(compute_sum_of_ti(array))
    # print(compute_sum_of_tj(array))
    # print(len(array))
    # print(len(array[0]))
    # tj=compute_sum_of_tj(array)
    # ti=compute_sum_of_ti(array)
    # T_2=compute_sum_of_t(array)
    # C=len(array[0])
    # R=len(array)
    # cf=(T_2*T_2)/(C*R)
    # sst=compute_sum_of_squares_in_array_of_arrays(array)-cf
    # ssc=compute_sum_of_squares_in_array(tj)/R-cf
    # ssr=compute_sum_of_squares_in_array(ti)/C-cf
    # sse=sst-ssc-ssr
    # ddlc=C-1
    # ddlr=R-1
    # ddle=ddlc*ddlr
    # msc=ssc/ddlc
    # msr=ssr/ddlr
    # mse=sse/ddle
    # fc=msc/mse
    # fr=msr/mse

    # print( f.ppf(1 - 0.05, 3, 6))
    # print(sst)
    # print(ssc)
    # print(ssr)
    # print(sse)
    # print(msc)
    # print(msr)
    # print(mse)
    # print(fc)
    # print(fr)

    ano=AnovaTwoWay(array)
    ano.datacontroller()
    print(ano.formHyp())
    print(ano.distribution())
    print(ano.steps(0.05))
    print(ano.testval())
    
    print(ano.conclusion())