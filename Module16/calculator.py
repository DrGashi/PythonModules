import streamlit as st

num1 = st.number_input("Enter the first digit: ")
num2 = st.number_input("Enter the second digit: ")
operator = st.text_input("Enter the operation you want to proceed with: ")

if operator == "+":
    st.write(f"The addition of {num1} and {num2} is equal to ", (num1 + num2))
elif operator == "-":
    st.write(f"The subtraction of {num1} and {num2} is equal to ", (num1 - num2))
elif operator == "*":
    st.write(f"The multiplication of {num1} and {num2} is equal to ", (num1 * num2))
elif operator == "/":
    try:
        st.write(f"The division of {num1} and {num2} is equal to ", (num1 / num2))
    except Exception as e:
        st.exception(e)
else:
    st.error("Please enter a valid operator")