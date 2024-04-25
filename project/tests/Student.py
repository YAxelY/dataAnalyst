from scipy import stats

# Exemple de données pour deux groupes
groupe1 = [23, 25, 28, 30, 54]
groupe2 = [20, 22, 25, 27, 29]

# Effectuer le test de Student (t-test) pour des échantillons indépendants
t_statistique, p_value = stats.ttest_ind(groupe1, groupe2)

# Afficher les résultats
print("Statistique de test t :", t_statistique)
print("P-value :", p_value)

# Interprétation des résultats
alpha = 0.05  # Niveau de signification
if p_value < alpha:
    print("La différence entre les moyennes est statistiquement significative (rejeter l'hypothèse nulle)")
else:
    print("Il n'y a pas de différence statistiquement significative entre les moyennes (ne pas rejeter l'hypothèse nulle)")
4