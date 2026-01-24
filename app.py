import streamlit as st

st.title("My First Streamlit App")
st.write("Hello Streamlit")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1)

if st.button("Submit"):
    st.write("Name:", name)
    st.write("Age:", age)

students = [
    {"name": "Arun", "age": 19},
    {"name": "Vinu", "age": 20}
]

st.table(students)
