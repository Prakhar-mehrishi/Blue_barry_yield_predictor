 import streamlit as st 
 from PIL import Image
 import pickle
 import numpy as np
 import matplotlib.pyplot as plt
 import pandas as pd
 st.set_option('deprecation.showfileUploaderEncoding', False)
 # Load the pickled model
 model = pickle.load(open('/content/drive/My Drive/rm_model.pkl', 'rb'))
 dataset= pd.read_csv('/content/drive/My Drive/WildBlueberryPollinationSimulationData.csv',)
 X = dataset.iloc[:, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]].values
 def predict_note_authentication(clonesize,honeybee,bumbles,andrena,osmia, MaxOfUpperTRange,MinOfUpperTRange,AverageOfUpperTRange,MaxOfLowerTRange,MinOfLowerTRange,AverageOfLowerTRange,RainingDays,AverageRainingDays,fruitset,fruitmass,seeds):
   output= model.predict([[clonesize,honeybee,bumbles,andrena,osmia, MaxOfUpperTRange,MinOfUpperTRange,AverageOfUpperTRange,MaxOfLowerTRange,MinOfLowerTRange,AverageOfLowerTRange,RainingDays,AverageRainingDays,fruitset,fruitmass,seeds]])
   print("The Predicted Yeald is = ", output)
   return output
 
 def main():
     
     html_temp = """
    <div class="" style="background-color:blue;" >
    <div class="clearfix">           
    <div class="col-md-12">
    <center><p style="font-size:40px;color:white;margin-top:10px;">The Machine Learning company</p></center> 
    <center><p style="font-size:30px;color:white;margin-top:10px;">Yield Predictor</p></center> 
    <center><p style="font-size:25px;color:white;margin-top:10px;"Blue Berry co.</p></center> 
    </div>
    </div>
    </div>
    """
     st.markdown(html_temp,unsafe_allow_html=True)
     st.header("Blue Berry Yield Pedictor ")
 
     clonesize = st.number_input("Insert Clonesize",0.0,40.0)
     honeybee = st.number_input("Insert no. of honeybee",0.0,18.5)
     bumbles = st.number_input("Insert no. of bumbles",0.0,0.5)
     andrena = st.number_input("Insert adrena",0.0,0.9)
     osmia = st.number_input("Insert osmia",0.0,0.91)
     MaxOfUpperTRange = st.number_input("Insert Max of Upper T Range",0.0,100.0)
     MinOfUpperTRange = st.number_input("Insert Min of Upper T Range",0.0,99.0)
     AverageOfUpperTRange = st.number_input("Insert Avg of Upper T Range",0.0,98.0)
     MaxOfLowerTRange = st.number_input("Insert Max of Lower T Range",0.0,101.0)
     MinOfLowerTRange = st.number_input("Insert Min of Lower T Range",0.0,102.0)
     AverageOfLowerTRange = st.number_input("Insert Avg of Lower T Range",0.0,103.0)
     RainingDays = st.number_input("Insert no. of rainy days",0.0,92.0)
     AverageRainingDays = st.number_input("Insert Avg Raining days",0.0,0.92)
     fruitset =  st.number_input("Insert Fruit set",0.0,0.93)
     fruitmass = st.number_input("Insert fruit mass",0.0,0.94)
     seeds = st.number_input("Insert seeds",0.0,50.0)
     result=""
 
     if st.button("Prediction"):
       result=predict_note_authentication(clonesize,honeybee,bumbles,andrena,osmia, MaxOfUpperTRange,MinOfUpperTRange,AverageOfUpperTRange,MaxOfLowerTRange,MinOfLowerTRange,AverageOfLowerTRange,RainingDays,AverageRainingDays,fruitset,fruitmass,seeds)
       st.success('The predicted yeild is {}'.format(result))
 
     if st.button("About"):
       st.header("By Prakhar Mehrishi")
       st.subheader("Intern , The Machine Learning Company")
     html_temp = """
     <div class="" style="background-color:orange;" >
     <div class="clearfix">           
     <div class="col-md-12">
     <center><p style="font-size:20px;color:white;margin-top:10px;">Yield Predictor</p></center> 
     </div>
     </div>
     </div>
     """
     st.markdown(html_temp,unsafe_allow_html=True)
 if __name__=='__main__':
   main()

