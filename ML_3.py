"""
Created on Sun Apr 30 21:39:50 2023

@author: Moaaz Elsadany
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

ada_model = pickle.load(open("ada_model.sav", 'rb'))

SVM_model = pickle.load(open("SVM_model.sav",'rb'))

DT_model = pickle.load(open("DT_model.sav", 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Diabetes Prediction Web App',
                          
                          ['AdaBoost',
                           'Support Vector Machines',
                           'DecisionTree'],
                          icons=['Logistic Regression','SVM','DT'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'AdaBoost'):
    
    # page title
    st.title('AIE121 - AdaBoost')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    ada_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('AdaBoost Regression Test Result'):
        ada_prediction = ada_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (ada_prediction[0] == 1):
          ada_diagnosis = 'The person is diabetic'
        else:
          ada_diagnosis = 'The person is not diabetic'
        
    st.success(ada_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Support Vector Machines'):
    
    # page title
   st.title('AIE121 - SVM')
    
   # getting the input data from the user
   col1, col2, col3 = st.columns(3)
   
   with col1:
       Pregnancies = st.text_input('Number of Pregnancies')
       
   with col2:
       Glucose = st.text_input('Glucose Level')
   
   with col3:
       BloodPressure = st.text_input('Blood Pressure value')
   
   with col1:
       SkinThickness = st.text_input('Skin Thickness value')
   
   with col2:
       Insulin = st.text_input('Insulin Level')
   
   with col3:
       BMI = st.text_input('BMI value')
   
   with col1:
       DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
   
   with col2:
       Age = st.text_input('Age of the Person')
        
        
     
     
    # code for Prediction
   SVM_diagnosis = ''
    
    # creating a button for Prediction
    
   if st.button('SVM Test Result'):
        SVM_prediction = SVM_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])                          
        
        if (SVM_prediction[0] == 1):
          SVM_diagnosis = 'The person is diabetic'
        else:
          SVM_diagnosis = 'The person is not diabetic'
        
   st.success(SVM_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "DecisionTree"):
    
    # page title
   st.title("AIE121 - Decision Tree")
    
   # getting the input data from the user
   col1, col2, col3 = st.columns(3)
   
   with col1:
       Pregnancies = st.text_input('Number of Pregnancies')
       
   with col2:
       Glucose = st.text_input('Glucose Level')
   
   with col3:
       BloodPressure = st.text_input('Blood Pressure value')
   
   with col1:
       SkinThickness = st.text_input('Skin Thickness value')
   
   with col2:
       Insulin = st.text_input('Insulin Level')
   
   with col3:
       BMI = st.text_input('BMI value')
   
   with col1:
       DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
   
   with col2:
       Age = st.text_input('Age of the Person')
        
    
    
    # code for Prediction
   DT_diagnosis = ''
    
    # creating a button for Prediction    
   if st.button("DT Test Result"):
        DT_prediction = DT_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])                          
        
        if (DT_prediction[0] == 1):
          DT_diagnosis = "The person is diabetic"
        else:
          DT_diagnosis = "The person is not diabetic"
        
   st.success(DT_diagnosis)
