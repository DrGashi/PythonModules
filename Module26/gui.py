import streamlit as st
import requests

st.title("Recipe App")
id = st.number_input("Recipe ID", 0, 100, 0, 1)
if id:
    response = requests.get(f"http://127.0.0.1:8000/recipes/?recipe_id={id}")
    if response.status_code == 200:
        st.write("Food:", response.json()["recipe"])
        st.write("Category:", response.json()["category"])
    else:
        st.error("Recipe not found!")