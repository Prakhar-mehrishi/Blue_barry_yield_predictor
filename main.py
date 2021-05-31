import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset= pd.read_csv('WildBlueberryPollinationSimulationData.csv')



# Extracting dependent and independent variables:
# Extracting independent variable:
X = dataset.iloc[:,1:17].values
# Extracting dependent variable:
y = dataset.iloc[:, 17].values



from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 5)


from sklearn.ensemble import RandomForestRegressor
model1 = RandomForestRegressor()
model1.fit(X_train, y_train)






