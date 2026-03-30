import streamlit as st

if st.number_input("Enter your age") >= 18:
    person = "Adult"
elif 0 <= st.number_input("Enter your age") < 18:
    person = "Child"
else:
    st.error("Please enter a valid age")
    person = ""
height = st.number_input("Enter the your height in m: ")
weight = st.number_input("Enter the your weight in kg: ")
if person == "Adult":
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        st.write("You are Underweight")
    elif 18.5 <= bmi < 24.9:
        st.write("You are Normal Weight")
    elif 24.9 <= bmi < 29.9:
        st.write("You are Overweight")
    elif bmi >= 29.9:
        st.write("You are Obese")
    else:
        st.error("Please enter a valid age to view your BMI Class")
elif person == "Child":
    bmi = (weight / (height ** 2)) * 1.3
    if bmi < 14:
        st.write("You are Underweight")
    elif 14 <= bmi < 18:
        st.write("You are Normal Weight")
    elif 18 <= bmi < 24:
        st.write("You are Overweight")
    elif bmi >= 24:
        st.write("You are Obese")
    else:
        st.error("Please enter a valid age to view your BMI Class")
else:
    bmi = 0
    st.error("Please enter a valid age to view your BMI")
