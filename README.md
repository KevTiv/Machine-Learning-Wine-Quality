MACHINE LEARNING WEB-APP 
WINE QUALITY PREDICTION APP

- Code written in python and data treated using jupyter notebook
- Model trainned with AutoML using TPOT Library
- Web application built with Streamlit library
- Application hosted on Heroku
- All dependences can be found in the requirements.txt

- The app purpose is to predict the quality of a wine sample
- User input wine variables and based on machine learning process
  the app offers its prediction on the quality of the wine.

- To run to program make sure to have all the required libraries installed:
  1. python3 -m venv venv
  2. source venv/bin/activate
  3. pip install -r requirements.txt 
  4. run in terminal app.py
  next in terminal write command " streamlit run app.py " 
  OR go directly to the web-app hosted on Heroku https://winequality-predictor.herokuapp.com

# Description

Web app project built to offer the possibility to grade wine quality according to the chemical 
composition of a wine sample. A user can adjust those chemical factors from a slider panel in the web application. 
The app grader model is built using machine learning techniques on a dataset that is consist of 1600 different wines.

# Goal

Build a web application That offers the end-user the possibility to grade the wine quality 
depending on the chemical content of the user’s wine.

# Challenges

Build an accurate grading model that will offer the user highly accurate predictions.

# Solution Implemented

The grading model is built in python (Jupyter Notebook). The model is trained using AutoML using 
the TPOT Library on the Vinho Verde dataset, available on Kaggle.com under the MIT library. The 
front end is built with the streamlit library because it simplified the process of building a front end 
for the app and, this python library is focused on offering components design and built around easy data visualization.

# Future Improvement

Build the front end of the web app using a JavaScript framework that is less opinionated and will 
enable a more creative approach to the look of the app and a better user experience.
