
import numpy as np
from scipy.stats import ttest_1samp, t
from scipy import stats
import scipy.stats


# Demander a l'utilisateur les parametres du test
n = int(input('entrer la taille de l\'echantillon:'))
mu_0 = float(input('entrer la moyenne théorique:'))
sigma = float(input('entrer l\'ecart-type de l\'echantillon:'))
X_bar = float(input('entrer la moyenne de l\'echantillon:'))
alpha = float(input('entrer le seuil de signification:'))
# Formuler l'hypothese nulle et alternative
hypothese_nulle = 'La moyenne de la population est egale à la moyenne theorique'
hypothese_alternative = 'La moyenne de la population est differente de la moyenne theorique'
# Collecter les donnees de l'echantillon
# calacul de la moyenne
mu = mu_0
# Formulation dhypotheses
# H0 : mu = mu_0
# H1 : mu!= mu_0
# Choix de la loi de probabilite
if mu > mu_0:
    test_type = "droite"
    print("il s\'agit d\'un test  unilateral à droite")
elif mu < mu_0:
    test_type = "gauche"
    print("il s\'agit d\'un test  unilateral à gauche")
else:
    test_type = "bilateral"
    print("il s\'agit d\'un test bilateral")
if n > 30:
    print('Comme la taille de l\'echantillon est superieure à 30, alors, on utilisera la loi normale telle que '
          'X_bar->N(mu;sigma^2)')
    S_X_bar = sigma / (n**0.5)
    print('Z=(X_bar-mu)/S_X_bar avec S_X_bar = sigma / (n**0.5) :', S_X_bar)
    # Valeur du test
    Z = (X_bar - mu) / (sigma / (n ** 0.5))
    print('la valeur d\'observation Z est:', Z)
else:
    print('Comme la taille de l\'echantillon est inferieure à 30, alors X_bar suit la loi de student')
    ddl = n-1
    # Calcul de la statistique de test (t-statistic)
    sample_std_error = sigma / np.sqrt(n)
    t_statistic = (X_bar - mu) / sample_std_error
    print('T_obs:',  t_statistic)
    # Niveau de signification alpha
    alpha = 0.05
    infini = '$'
    # Calcul du point critique (valeur t critique)
    critical_value = t.ppf(1 - alpha / 2, n - 1)
    critical_value_1 = t.ppf(alpha, n - 1)
    critical_value_2 = -t.ppf(alpha, n - 1)
    # Pour un test bilatéral
    # Calcul de l'intervalle de non-rejet de H0
    if test_type == "bilateral":
        print('T_crit:', critical_value)
        print('INRH0 =:', [-critical_value, critical_value])
        INRH0 = [-critical_value, critical_value]
    elif test_type == "droite":
        print('T_crit:', critical_value_1)
        print('INRH0 =:', [-infini, critical_value_1])
        INRH0 = [-infini, critical_value_1]
    else:
        print('T_crit:', critical_value_2)
        print('INRH0 =:', [critical_value_2, +infini])
        INRH0 = [critical_value_2, +infini]
    if t_statistic not in INRH0:
        print('Comme T_obs est dans inrH0, alors on accepte H0')
    else:
        print('Comme T_obs n\'est pas dans inrH0,alors on rejette H0')
    # Calcul du point critique
if n > 30:
    # Calcul du seuil de signification
    alpha_one_tail = alpha / 2
    infini = '$'
    # Calcul de la valeur critique
    critiqual_value_one_tail = stats.norm.ppf(1-alpha_one_tail)
    critiqual_value_one_tail_1 = stats.norm.ppf(1 - alpha)
    # Calcul du point critique pour un test bilateral
    critical_value_two_tails = critiqual_value_one_tail
    critical_value_two_tails_2 = critiqual_value_one_tail_1
    print('Point critique Zobs:', critical_value_two_tails)
    limite_inferirure = -critical_value_two_tails
    limite_superieure = critical_value_two_tails
    if test_type == "bilateral":
        print(f"L'intervalle de non rejet de l'hypothese nulle H0 est:[{-critical_value_two_tails} , {critical_value_two_tails}]")
        inrH0 = [{-critical_value_two_tails}, {critical_value_two_tails}]
    elif test_type == "droite":
        print(f'L\'intervalle de non rejet de l\'hypothese nulle H0 est:[{-infini} , {critical_value_two_tails_2}]')
        inrH0 = [{-infini} , {critical_value_two_tails_2}]
    else:
        print(f'L\'intervalle de non rejet de l\'hypothese nulle H0 est:[{critical_value_two_tails_2}, {+infini}]')
        inrH0 = [{critical_value_two_tails_2}, {+infini}]
        # prise de decision et conclusion
    Z = (X_bar - mu) / (sigma / (n ** 0.5))
    if Z not in inrH0:
        print('Comme Z est dans inrH0, alors on accepte H0')
    else:
        print('Comme Z n\'est pas dans inrH0,alors on rejette H0')
   

