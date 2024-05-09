AnovaOneWay||||5 4 8 6 3
9 7 8 6 9
3 5 2 3 7
2 3 4 1 4 
7 6 9 4 7|α_j est l'effet sur les colonnes
H0: α_1 = α_2 = α_3 = α_4 = α_5
H1: Au moins une des moyennes sur les colonnes diffère des autres
|On utilise la loi de Fisher (F-distribution) 
|INRH0: [0, 2.8660814020156584]

|+------------------------+--------------------+------------------+----------------------+-------------------+
|  source de variation   | sommes des carrés  | dégré de liberté | carrées des moyennes |   valeur du test  |
+------------------------+--------------------+------------------+----------------------+-------------------+
| effet sur les colonnes | 79.44000000000005  |        4         |  19.860000000000014  | 6.895833333333349 |
|         erreur         | 57.59999999999991  |        20        |  2.8799999999999955  |        NaN        |
|         total          | 137.03999999999996 |        24        |         NaN          |        NaN        |
+------------------------+--------------------+------------------+----------------------+-------------------+
|Nous rejetons l'hypothèse nulle (H0). Au risque de se tromper de 5.0%, il y a une différence significative entre les moyennes des groupes.
|