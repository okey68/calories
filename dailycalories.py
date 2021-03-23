import streamlit as st
import time

#Header&Title
st.header('Find Your Daily Calories')
st.subheader('How many calories should you eat in a day?')
#inputs
#Gender
gender = st.selectbox('Gender', ['Female','Male'])
#Age
age = st.number_input('Age',0)
#Height
height = st.number_input('Height (inches)',60)
#Weight
weight = st.number_input('Weight (pounds)',60)
#Daily Activity
activity = st.selectbox('Activity Level',['Sedentary','Lightly Active','Moderately Active','Very Active','Super Active'])
actDict = {'Sedentary':1.2,'Lightly Active':1.3,'Moderately Active':1.5,'Very Active':1.7,'Super Active':1.9}



#Formula
#Adult male: 66 + (6.3 x body weight in lbs.) + (12.9 x height in inches) - (6.8 x age in years) = BMR
#Adult female: 655 + (4.3 x weight in lbs.) + (4.7 x height in inches) - (4.7 x age in years) = BMR

if gender == 'Male':
    BMR = round(66 + (6.3 * weight) + (12.9 * height) - (6.8 * age),2)
    cals = round(BMR * actDict[activity],2)
    time.sleep(1.5)
    st.write("""
    ## Your daily BMR is:""")
    st.write(BMR, 'calories')
    time.sleep(1)
    st.write("""
    ## Your daily calories intake should be:""")
    st.write(cals, 'calories')
    
else:
    BMR = round(655 + (4.3 * weight) + (4.7 * height) - (4.7 * age),2)
    cals = round(BMR * actDict[activity],2)
    time.sleep(1.5)
    st.write("""
    ## Your daily BMR is:""")
    st.write(BMR, 'calories')
    time.sleep(1)
    st.write("""
    ## Your daily calories intake should be:""")
    st.write(cals, 'calories')






