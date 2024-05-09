# Importing libraries 
import pandas as pd
import numpy as np
import statsmodels.api as sm 
from statsmodels.formula.api import ols 

# Create a dataframe 
dataframe = pd.DataFrame({'Fertilizer': np.repeat(['daily', 'weekly'], 15), 
						'Watering': np.repeat(['group1', 'group2','group3'], 10), 
						'height': [14, 16, 15, 15, 16, 13, 12, 11, 
									14, 15, 16, 16, 17, 18, 14, 13, 
									14, 14, 14, 15, 16, 16, 17, 18, 
									14, 13, 14, 14, 14, 15]}) 


# Performing two-way ANOVA 
model = ols('height ~ C(Fertilizer) + C(Watering) + C(Fertilizer):C(Watering)', data=dataframe).fit() 
result = sm.stats.anova_lm(model, type=2) 
print(dataframe)
# Print the result 
print(result) 
