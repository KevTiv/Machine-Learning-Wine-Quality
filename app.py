import numpy as np 
import pandas as pd 
import joblib
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import streamlit as st
import streamlit_analytics
from PIL import Image
from random import randrange
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix as cm

# Wine Quality predictor
# This web-app use machine learning techniques to predict wine quality

# Create a copy of the user input
def data_preprocessor(df):
    """this function preprocess the user input
        return type: pandas dataframe
    """
    return df


def get_user_input():
    """
    this function is used to get user input using the sidebar selectbox 
    input are entered using slider for each category
    return type : pandas dataframe
    """
    fixed_acidity = st.sidebar.slider('fixed acidity (g / dm^3) ', 2.00, 18.00, 7.3)  
    volatile_acidity = st.sidebar.slider('volatile acidity  (g / dm^3) ', 0.05, 2.50, 0.65)  
    citric_acid  = st.sidebar.slider('citric acid  (g / dm^3) ', 0.00, 2.00, 0.00)  
    residual_sugar  = st.sidebar.slider('residual_sugar  (g / dm^3) ', 0.50, 70.00, 1.20)  
    chlorides  = st.sidebar.slider('chlorides  (g / dm^3) ', 0.005, 0.700, 0.065)  
    free_sulfur_dioxide = st.sidebar.slider('free sulfur dioxide  (mg / dm^3) ', 1.00, 300.00, 15.00)  
    total_sulfur_dioxide = st.sidebar.slider('total sulfur dioxide', 5.00, 440.00, 21.00)  
    density = st.sidebar.slider('density  (g / cm^3) ', 0.50, 2.00, 0.9946)  
    pH = st.sidebar.slider('pH', 1.00, 5.00, 2.29)  
    sulphates = st.sidebar.slider('sulphates  (g / dm^3) ', 0.10, 2.00, 0.47)  
    alcohol = st.sidebar.slider('alcohol  (%) ', 6.00, 16.00, 10.00)  
    
    features = {
            'fixed_acidity': fixed_acidity,
            'volatile_acidity': volatile_acidity,
            'citric_acid': citric_acid,
            'residual_sugar': residual_sugar,
            'chlorides': chlorides,
            'free_sulfur_dioxide': free_sulfur_dioxide,
            'total_sulfur_dioxide': total_sulfur_dioxide,
            'density': density,
            'pH': pH,
            'sulphates': sulphates,
            'alcohol': alcohol
            }
    data = pd.DataFrame(features,index=[0])

    return data


def main():

    # track web app activity
    streamlit_analytics.start_tracking()

    # Web Page Headers
    st.write("""
    # Wine Quality Prediction Web-App 
    This app predicts the ** Quality of your Red Wine **  using **wine features** input via the **side panel** 
    """)
    #read in wine image and render with streamlit
    image = Image.open('resources/wine_image.jpg')
    st.image(image, caption='The Wine Grader Company',use_column_width=True)
    st.sidebar.header('User Input Parameters') #user input parameter collection with streamlit side bar


    # Load  ML models  
    model_knn = joblib.load(open("model/autoML-model_knn.joblib","rb"))
    model_decis_tree = joblib.load(open("model/autoML-model_Decision-Tree.joblib","rb"))
    model_log_reg = joblib.load(open("model/autoML-model_Log-Regress.joblib","rb"))

    # user input variables
    user_input_df = get_user_input()
    processed_user_input = data_preprocessor(user_input_df)


    st.subheader('User Input parameters')
    st.write(user_input_df)

    # machine learning techniques results variables
    prediction_knn = model_knn.predict(processed_user_input)

    prediction__decis_tree = model_decis_tree.predict(processed_user_input)

    prediction_log_reg = model_log_reg.predict(processed_user_input)

    # output machine learning results
    st.write("Ask our A.I. wine connaisseur for their opinion")
    connaisseur_choice = st.selectbox("Connaisseur opinion: ", ['', 'The decision tree connaisseur',
    'The KNN connaisseur', 'The logistic regression connaisseur'])

    # A.I opinion displayed
    if (connaisseur_choice == "The decision tree connaisseur"):
        st.write("The decision tree connaisseur verdict: ")
        if(prediction__decis_tree == 1):
            st.write("Good quality wine! This wine is at least a 7 in my expert opinion. You got great test!")
        
            choose_image = randrange(1)
            if (choose_image == 1):
                image = Image.open('resources/wineconnaisseur_1.png')
                st.image(image,use_column_width=True)
            else:
                image = Image.open('resources/wineconnaisseur_3.png')
                st.image(image,use_column_width=True)
        else:
            st.write("Bad quality wine! Do yourself a favor and throw away this thing you call wine....")
            image = Image.open('resources/wineconnaisseur_2.png')
            st.image(image,use_column_width=True)

    if (connaisseur_choice == "The KNN connaisseur"):
        st.write("The KNN connaisseur verdict: ")
        if(prediction_knn == 1):
            st.write("Good quality wine! This wine is at least a 7 in my expert opinion. You got great test!")
            choose_image = randrange(1)
            if (choose_image == 0):
                image = Image.open('resources/wineconnaisseur_1.png')
                st.image(image,use_column_width=True)
            else:
                image = Image.open('resources/wineconnaisseur_3.png')
                st.image(image,use_column_width=True)
        else:
            st.write("Bad quality wine! Do yourself a favor and throw away this thing you call wine....")
            image = Image.open('resources/wineconnaisseur_2.png')
            st.image(image,use_column_width=True)

    if (connaisseur_choice == "The logistic regression connaisseur"):
        st.write("The logistic regression connaisseur verdict: ")
        if(prediction_log_reg == 1):
            st.write("Good quality wine! This wine is at least a 7 in my expert opinion. You got great test!")
            choose_image = randrange(1)
            if (choose_image == 1):
                image = Image.open('resources/wineconnaisseur_1.png')
                st.image(image,use_column_width=True)
            else:
                image = Image.open('resources/wineconnaisseur_3.png')
                st.image(image,use_column_width=True)
        else:
            st.write("Bad quality wine! Do yourself a favor and throw away this thing you call wine....")
            image = Image.open('resources/wineconnaisseur_2.png')
            st.image(image,use_column_width=True)

    # end tracking code block
    streamlit_analytics.stop_tracking()


if __name__ == '__main__':
    main()
