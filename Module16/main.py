import streamlit as st

# def main():
#     st.title("Hello World!")
#     st.button("Click me!")
#
# if __name__ == "__main__":
#         main()

if st.button("Click me!"):
    st.write("Button Clicked")
if st.checkbox("Show text"):
    st.write("text")
user_input = st.text_input("Enter text", "Sample Text")
st.write("You entered: ", user_input)

age = st.number_input("Enter age:", min_value=0, max_value=100)
st.write("Your age is: ", age)

message = st.text_area("Enter a message")
st.write("Your message: ", message)

choice = st.radio("Gender", ["Male", "Female", "Prefer not to say"])
st.write("Gender: ", choice)

if st.button("Success"):
    st.success("Operation successful")

try:
    1/0
except Exception as e:
    st.exception(e)