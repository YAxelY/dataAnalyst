from scipy.stats import f_oneway
from scipy.stats import f

class AnovaOneWay:
    def __init__(self, data_set):
        self.data = data_set
        
    def datacontroller(self):
        if len(self.data) > 1:
            # Implement your data handling logic here
            pass
    
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
    
    def dataEntry(self):
        # Implement data entry GUI components here
        pass
    
    def my_function(self, my_arg1, my_arg2):
        # Implement your custom function logic here
        pass
