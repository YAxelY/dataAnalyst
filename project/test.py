from scipy.stats import kruskal, chi2
from data_file import data  # Import des données depuis le fichier de données


# Variable contenant les différents groupes de données à tester
# Vous pouvez modifier ces données pour effectuer différents tests

def perform_kruskal_wallis_test(data):
    """ Fonction pour effectuer le test de Kruskal-Wallis sur les données fournies """
    if len(data) > 1:
        # Exécuter le test de Kruskal-Wallis
        stat, p_value = kruskal(*data)
        alpha = 0.05  # Seuil de signification
        df = len(data) - 1  # Degrés de liberté pour le test du chi-carré
        critical_value = chi2.ppf(1 - alpha, df=df)
        
        # Déterminer l'intervalle de non-rejet pour la statistique de test
        lower_bound = 0  # Le chi-carré est toujours positif, donc commence à 0
        upper_bound = critical_value  # Le seuil critique du chi-carré
        
        #Affichage des résultats
        print(f'Valeur de la statistique de test : {stat:.4f}')
        print(f'Valeur critique pour chi-carré avec {df} degrés de liberté : {critical_value:.4f}')
        print(f'Région de non-rejet : [{lower_bound:.4f}, {upper_bound:.4f}]')
        print(f'Valeur p : {p_value:.4f}')
        
        # Conclusion basée sur la valeur p
        if p_value < alpha:
            print("Nous rejetons l'hypothèse nulle (H0). Il y a une différence significative entre les médianes des groupes.")
        else:
            print("Nous n'avons pas suffisamment de preuves pour rejeter l'hypothèse nulle (H0). Les médianes des groupes sont statistiquement similaires.")
    else:
        print("Veuillez fournir des données pour au moins deux groupes pour effectuer le test de Kruskal-Wallis.")

# Appel de la fonction avec les données prédéfinies
perform_kruskal_wallis_test(data)
