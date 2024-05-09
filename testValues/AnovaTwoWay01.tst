AnovaTwoWay|||0.05|64 72 74
55 57 47
59 66 58
58 57 53|α_i est l'effet sur les lignes
β_j est l'effet sur les colonnes
H0: α_1 = α_2 = α_3 = α_4
H0': β_1 = β_2 = β_3
H1: Au moins une des moyennes sur les lignes diffère des autres
H1': Au moins une des moyennes sur les colonnes diffère des autres
|On utilise la loi de Fisher (F-distribution) car ANOVA à deux facteurs sans replications
|+------------------------+-------------------+------------------+----------------------+--------------------+
|  source de variation   | sommes des carrés | dégré de liberté | carrées des moyennes |   valeur du test   |
+------------------------+-------------------+------------------+----------------------+--------------------+
| effet sur les colonnes |        56.0       |        2         |         28.0         | 1.5555555555555556 |
|  effet sur les lignes  |       498.0       |        3         |        166.0         | 9.222222222222221  |
|         erreur         |       108.0       |        6         |         18.0         |        NaN         |
|         total          |       662.0       |        11        |         NaN          |        NaN         |
+------------------------+-------------------+------------------+----------------------+--------------------+
|INRH0: [0, 4.757062663089414]
INRH0': [0, 5.143252849784718]
|Nous acceptons l'hypothèse nulle (H0) pour les effets sur les lignes, mais nous rejetons l'hypothèse nulle (H0') pour les effets sur les colonnes.  Au risque de se tromper de 5.0%, Il y a une différence significative entre les moyennes des groupes pour les effets sur les colonnes.
|