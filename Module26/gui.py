import streamlit as st
import requests

st.title("Recipe App")

page = st.sidebar.selectbox("Select what you want to do!",["Get Recipe", "Update Recipe", "Create Recipe", "Delete Recipe"])

if page == "Get Recipe":
    id = st.number_input("Recipe ID", 0, 100, 0, 1)
    if id:
        response = requests.get(
            f"http://127.0.0.1:8000/recipes/?recipe_id={id}"
        )
        if response.status_code == 200:
            st.write("Food:", response.json()["recipe"])
            st.write("Category:", response.json()["category"])
        else:
            st.error("Recipe not found!")

elif page == "Update Recipe":
    id = st.number_input("Recipe ID", 0, 100, 0, 1)
    food = st.text_input("Food")
    category = st.text_input("Category")
    submit = st.button("Update")
    if submit:
        response = requests.put(
            f"http://127.0.0.1:8000/recipes/?recipe_id={id}",
            json={
                "recipe": food,
                "category": category
            }
        )
        if response.status_code == 200:
            st.success("Recipe Updated Successfully!")
            st.write("Food:", response.json()["recipe"])
            st.write("Category:", response.json()["category"])
        else:
            st.error("Recipe not found!")

elif page == "Create Recipe":
    food = st.text_input("Food")
    category = st.text_input("Category")
    submit = st.button("Create Recipe")
    if submit:
        response = requests.post(
            f"http://127.0.0.1:8000/recipes/",
            json={
                "recipe": food,
                "category": category,
                "id": 0
            }
        )
        st.success("Recipe Created Successfully!")

elif page == "Delete Recipe":
    id = st.number_input("Recipe ID", 0, 100, 0, 1)
    submit = st.button("Delete Recipe")
    if submit:
        response = requests.delete(
            f"http://127.0.0.1:8000/recipes/?recipe_id={id}"
        )
        if response.status_code == 200:
            st.success("Recipe not found!")
        else:
            st.success("Recipe Deleted Successfully!")