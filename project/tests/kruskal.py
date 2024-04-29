from scipy.stats import kruskal, chi2

class Kruskal:
    def __init__(self,dataSet):
        self.data = dataSet
        
    def datacontroller(self):
        if len(self.data) > 1:
            
            self.stat, self.p_value = kruskal(*self.data)
    #commun interfaces
    def formHyp(self):

        n=len(self.data)
        symbol = "θ²"
        hypothesis_string = "H0: "
        for i in range(1, n+ 1):
            if i > 1:
                hypothesis_string += "="
            hypothesis_string += symbol + "_{}".format(i)

      


        
        
        return hypothesis_string+ "\nH_1: Au moins une moyenne diffère des autres"
    
    def distribution(self):
        

       return "on utise la loi de kruskal-Wallis"
    

    def testval(self):
        
        return "p-value: "+str(self.p_value)
    

    
    def steps(self,alpha):

        alpha = float(alpha)

        df = len(self.data) - 1  # Degrés de liberté pour le test du chi-carré
        critical_value = chi2.ppf(1 - alpha, df=df)
        
        # Déterminer l'intervalle de non-rejet pour la statistique de test
        lower_bound = 0  # Le chi-carré est toujours positif, donc commence à 0
        upper_bound = critical_value  # Le seuil critique du chi-carré

        stat_string = f'Valeur de la statistique de test : {self.stat:.4f}'+"\n"
        critical_value_string = f'Valeur critique pour chi-carré avec {df} degrés de liberté : {critical_value:.4f}'+"\n"
        region_string = f'Région de non-rejet : [{lower_bound:.4f}, {upper_bound:.4f}]'+"\n"
        p_value_string = f'Valeur p : {self.p_value:.4f}'+"\n"
        string=stat_string+critical_value_string+region_string+p_value_string
        return string
        
    def conclusion(self,alpha = 0.05,desc=""):

        alpha = float(alpha)
        desc= str(desc)
        if self.p_value < alpha:
            return "Nous rejetons l'hypothèse nulle (H0). Il y a une différence significative entre les médianes des groupes."
        else:
            return "Nous n'avons pas suffisamment de preuves pour rejeter l'hypothèse nulle (H0). Les médianes des groupes sont statistiquement similaires."
    
    #personnal function
    def N(self):
        N=0
        for i in self.dataSet:
            N+=len(i)
                       

    

       


if __name__ == '__main__':
    pass