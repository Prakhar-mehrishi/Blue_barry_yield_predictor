# -*- coding: utf-8 -*-
"""ML_First_assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MUgrgDn-msVuBdMrqYNL-mg0wHGHIdW-
"""

# # Data Preprocessing
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

from google.colab import files
Uploaded=files.upload()

dataset= pd.read_csv('WildBlueberryPollinationSimulationData.csv')
print(dataset)

print(dataset.shape)

dataset.info()

# Extracting dependent and independent variables:
# Extracting independent variable:
X = dataset.iloc[:,1:17].values
# Extracting dependent variable:
y = dataset.iloc[:, 17].values

dataframe=pd.DataFrame(X,columns=['clonesize','honeybee','bumbles','andrena', 'osmia', 'MaxOfUpperTRange', 'MinOfUpperTRange','AverageOfUpperTRange','MaxOfLowerTRange','MinOfLowerTRange',
                                  'AverageOfLowerTRange', 'RainingDays','AverageRainingDays' , 'fruitset' ,'fruitmass' ,'seeds'])
dataframe.isnull().sum()

print(X)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 5)

print(X_train)

print(X_test)

print(y_test)

print(y_train)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print(X_train)

print(X_test)

from sklearn.ensemble import RandomForestRegressor
model1 = RandomForestRegressor()
model1.fit(X_train, y_train)

y_pred = model1.predict(X_test)
print(y_pred)

from sklearn import metrics
print("MAE %2.f" %(metrics.mean_absolute_error(y_test,y_pred)))

from sklearn import metrics
print("RMSE %2.f" %(np.sqrt(metrics.mean_absolute_error(y_test,y_pred))))



loaded_model = joblib.load(filename)
result = loaded_model.score(X_test, y_test)
print(result)

clonesize = 37.5#@param {type:"number"}
honeybee = 0.25#@param {type:"number"}
bumbles = 0.25#@param {type:"number"}
andrena = 0.25#@param {type:"number"}
osmia = 0.25#@param {type:"number"}
MaxOfUpperTRange = 80.4#@param {type:"number"}
MinOfUpperTRange = 42.1#@param {type:"number"}
AverageOfUpperTRange = 42.1#@param {type:"number"}
MaxOfLowerTRange = 55.8#@param {type:"number"}
MinOfLowerTRange = 27.1#@param {type:"number"}
AverageOfLowerTRange = 45.8#@param {type:"number"}
RainingDays = 3#@param {type:"number"}
AverageRainingDays = 0.26#@param {type:"number"}
fruitset =  0.39254#@param {type:"number"}
fruitmass = 0.39#@param {type:"number"}
seeds = 30.88504716#@param {type:"number"}

output= model1.predict([[clonesize,honeybee,bumbles,andrena, osmia, MaxOfUpperTRange, MinOfUpperTRange,AverageOfUpperTRange,MaxOfLowerTRange,MinOfLowerTRange,AverageOfLowerTRange, RainingDays,AverageRainingDays,fruitset,fruitmass,seeds]])
print("yield score:", output)



# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st 
# from PIL import Image
# import pickle
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# st.set_option('deprecation.showfileUploaderEncoding', False)
# # Load the pickled model
# model = pickle.load(open('/content/drive/My Drive/rm_model.pkl', 'rb'))
# dataset= pd.read_csv('/content/drive/My Drive/WildBlueberryPollinationSimulationData.csv',)
# X = dataset.iloc[:, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]].values
# def predict_note_authentication(clonesize,honeybee,bumbles,andrena,osmia, MaxOfUpperTRange,MinOfUpperTRange,AverageOfUpperTRange,MaxOfLowerTRange,MinOfLowerTRange,AverageOfLowerTRange,RainingDays,AverageRainingDays,fruitset,fruitmass,seeds):
#   output= model.predict([[clonesize,honeybee,bumbles,andrena,osmia, MaxOfUpperTRange,MinOfUpperTRange,AverageOfUpperTRange,MaxOfLowerTRange,MinOfLowerTRange,AverageOfLowerTRange,RainingDays,AverageRainingDays,fruitset,fruitmass,seeds]])
#   print("The Predicted Yeald is = ", output)
#   return output
# 
# def main():
#     
#     html_temp = """
#    <div class="" style="background-color:blue;" >
#    <div class="clearfix">           
#    <div class="col-md-12">
#    <center><p style="font-size:40px;color:white;margin-top:10px;">The Machine Learning company</p></center> 
#    <center><p style="font-size:30px;color:white;margin-top:10px;">Yield Predictor</p></center> 
#    <center><p style="font-size:25px;color:white;margin-top:10px;"Blue Berry co.</p></center> 
#    </div>
#    </div>
#    </div>
#    """
#     st.markdown(html_temp,unsafe_allow_html=True)
#     st.header("Blue Berry Yield Pedictor ")
# 
#     clonesize = st.number_input("Insert Clonesize",0.0,40.0)
#     honeybee = st.number_input("Insert no. of honeybee",0.0,18.5)
#     bumbles = st.number_input("Insert no. of bumbles",0.0,0.5)
#     andrena = st.number_input("Insert adrena",0.0,0.9)
#     osmia = st.number_input("Insert osmia",0.0,0.91)
#     MaxOfUpperTRange = st.number_input("Insert Max of Upper T Range",0.0,100.0)
#     MinOfUpperTRange = st.number_input("Insert Min of Upper T Range",0.0,99.0)
#     AverageOfUpperTRange = st.number_input("Insert Avg of Upper T Range",0.0,98.0)
#     MaxOfLowerTRange = st.number_input("Insert Max of Lower T Range",0.0,101.0)
#     MinOfLowerTRange = st.number_input("Insert Min of Lower T Range",0.0,102.0)
#     AverageOfLowerTRange = st.number_input("Insert Avg of Lower T Range",0.0,103.0)
#     RainingDays = st.number_input("Insert no. of rainy days",0.0,92.0)
#     AverageRainingDays = st.number_input("Insert Avg Raining days",0.0,0.92)
#     fruitset =  st.number_input("Insert Fruit set",0.0,0.93)
#     fruitmass = st.number_input("Insert fruit mass",0.0,0.94)
#     seeds = st.number_input("Insert seeds",0.0,50.0)
#     result=""
# 
#     if st.button("Prediction"):
#       result=predict_note_authentication(clonesize,honeybee,bumbles,andrena,osmia, MaxOfUpperTRange,MinOfUpperTRange,AverageOfUpperTRange,MaxOfLowerTRange,MinOfLowerTRange,AverageOfLowerTRange,RainingDays,AverageRainingDays,fruitset,fruitmass,seeds)
#       st.success('The predicted yeild is {}'.format(result))
# 
#     if st.button("About"):
#       st.header("By Prakhar Mehrishi")
#       st.subheader("Intern , The Machine Learning Company")
#     html_temp = """
#     <div class="" style="background-color:orange;" >
#     <div class="clearfix">           
#     <div class="col-md-12">
#     <center><p style="font-size:20px;color:white;margin-top:10px;">Yield Predictor</p></center> 
#     </div>
#     </div>
#     </div>
#     """
#     st.markdown(html_temp,unsafe_allow_html=True)
# if __name__=='__main__':
#   main()



