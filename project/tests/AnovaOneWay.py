from scipy.stats import f_oneway
from scipy.stats import f
# <<<<<<< HEAD

# =======
from prettytable import PrettyTable
from tkinter import messagebox
# >>>>>>> 228a0535364e44925f000f0c17fab78e22bc51d7
class AnovaOneWay:
    def __init__(self, data_set):
        self.data = data_set
        
    def datacontroller(self):
# <<<<<<< HEAD
        if len(self.data) > 1:
            self.p_value,_ = f_oneway(*self.data) 
            
    
    def formHyp(self):
        n = len(self.data)
        symbol = "θ²"
        hypothesis_string = "H0: "
        for i in range(1, n+ 1):
            if i > 1:
                hypothesis_string += "="
            hypothesis_string += symbol + "_{}".format(i)
        
        return hypothesis_string + "\nH_1: Au moins une moyenne diffère des autres"
    
    def distribution(self):
        return "On utilise la loi de Fisher (F-distribution)"
    
    def testval(self):
        # Calculate F-statistic value
        f_statistic, _ = f_oneway(*self.data) 
        return "F-statistic: {:.4f}".format(f_statistic)
    
    def steps(self, alpha):
        alpha = float(alpha)
        df_between = len(self.data) - 1
        df_within = sum(len(group) for group in self.data) - len(self.data)
        
        critical_value = f.ppf(1 - alpha, df_between, df_within)
        
        return "Critical value for F-distribution with df({}, {}) : {:.4f}".format(df_between, df_within, critical_value)
    
    def conclusion(self, alpha=0.05, desc=""):
        alpha = float(alpha)
        if self.p_value < alpha:
            return "Nous rejetons l'hypothèse nulle (H0). Il y a une différence significative entre les moyennes des groupes."
        else:
            return "Nous n'avons pas suffisamment de preuves pour rejeter l'hypothèse nulle (H0). Les moyennes des groupes sont statistiquement similaires."
    
# =======
        self.data = [sublist for sublist in self.data if sublist]
       
        self.ti=self.compute_sum_of_ti( self.data)
       
        self.T_2=self.compute_sum_of_t( self.data)
        self.c=len( self.data)
      
        self.ni=self.lengths_of_subarrays(self.data)
 
       
        self.cf=(self.T_2*self.T_2)/sum(self.ni)
      
        self.sst=self.compute_sum_of_squares_in_array_of_arrays( self.data)-self.cf
       
        self.ssc=self.square_items(self.ti)
        self.ssc=self.divide_corresponding_items(self.ssc,self.ni)
        self.ssc=sum(self.ssc)-self.cf
        

        self.sse=self.sst-self.ssc
     
        self.ddlc=self.c-1
     
        self.ddlt=sum(self.ni)-1
        
        self.ddle=(sum(self.ni)-1)-(self.c-1)
 
        self.msc=self.ssc/self.ddlc

   
        self.mse=self.sse/self.ddle
        self.fc=self.msc/self.mse
      
        
            
            
    def formHyp(self):
        # Constructing the null and alternative hypotheses
        symbol_alpha = "α"
        
        hypothesis_string = ""
        
        # Null hypothesis H0
        
        hypothesis_string += f"{symbol_alpha}_j est l'effet sur les colonnes\n"
        hypothesis_string += "H0: "
        for i in range(1, self.c+1):
            if i > 1:
                hypothesis_string += " = "
            hypothesis_string += symbol_alpha + "_{}".format(i)
       
      
        
        # Alternative hypothesis H1
        hypothesis_string += "\nH1: Au moins une des moyennes sur les colonnes diffère des autres"
        
    
        return hypothesis_string



    
    def distribution(self):
        return "On utilise la loi de Fisher (F-distribution) "
    
    def testval(self):
        return str(self.generate_pretty_table(self.ssc,self.ddlc,self.msc,self.fc,self.sse,self.ddle,self.mse,self.sst,self.ddlt))
    
    def steps(self, alpha):
        alpha=float(alpha)
        self.upper_bound_INRH0 = f.ppf(1 - alpha, self.ddlc, self.ddle)
        result = ""
        result += f"INRH0: [0, {self.upper_bound_INRH0}]\n"
      
        return result



        
    def conclusion(self, alpha=0.05,desc=""):
        if self.fc > self.upper_bound_INRH0:
            return f"Nous rejetons l'hypothèse nulle (H0). Au risque de se tromper de {alpha}%, il y a une différence significative entre les moyennes des groupes."
        else:
            return f"Nous acceptons l'hypothèse nulle (H0). Au risque de se tromper de {alpha}%, les moyennes des groupes sont statistiquement similaires."

# >>>>>>> 228a0535364e44925f000f0c17fab78e22bc51d7
    def dataEntry(self):
        # Implement data entry GUI components here
        pass
    
    def my_function(self, my_arg1, my_arg2):
        # Implement your custom function logic here
        pass
# <<<<<<< HEAD
# =======



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

    def generate_pretty_table(self,ssc, c_minus_1, msc, fc,sse,ddle, mse, sst, cr_minus_2):
        table = PrettyTable(["source de variation", "sommes des carrés", "dégré de liberté", "carrées des moyennes", "valeur du test"])
        table.add_row(["effet sur les colonnes", ssc, c_minus_1, msc, fc])
        
        table.add_row(["erreur", sse,ddle , mse, "NaN"])
        table.add_row(["total", sst, cr_minus_2, "NaN", "NaN"])
        return table
    def lengths_of_subarrays(self,array_of_arrays):
        return [len(sub_array) for sub_array in array_of_arrays]
    def square_items(self,array):
        return [item ** 2 for item in array]
    def divide_corresponding_items(self,array1, array2):
        if len(array1) != len(array2):
            raise ValueError("Arrays must have the same length")
        
        return [a / b for a, b in zip(array1, array2)]

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

        
# E1=[5,4,8,6,3]
# E2=[9,7,8,6,9]
# E3=[3,5,2,3,7]
# E4=[2,3,4,1,4]
# E5=[7,6,9,4,7]
# array=[E1,E2,E3,E4,E5]        
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

# ano=AnovaOneWay(array)
# ano.datacontroller()
# print(ano.formHyp())
# print(ano.distribution())
# print(ano.testval())
# print(ano.steps(0.05))
# print(ano.conclusion())
# >>>>>>> 228a0535364e44925f000f0c17fab78e22bc51d7
