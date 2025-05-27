import streamlit as st

st.title("Title: Bio Data")
st.write("This is sample web app.")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
gender = st.selectbox("gender", ["Male", "Female"])
age = st.number_input("Your Age", 0, 100, 30, 1)
dob = st.date_input("Your Birthday")
marital_cousin = st.radio("Marital Status", ["Single", "Married"])
years_of_experience = st.slider("Years of experience", 0, 40)



