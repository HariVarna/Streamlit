import streamlit as st
import pandas as pd

# Keep layout simple and centered
st.set_page_config(
    page_title="Student Manager",
    layout="centered"
)

st.title("Student Management System")
st.caption("Built with the same ideas shown in app.py: inputs, session_state, and tables.")

# Initialize session_state storage
if "students" not in st.session_state:
    st.session_state.students = []

students = st.session_state.students

st.divider()

# Section 1: Add student (similar to app.py inputs)
st.subheader("1.Add Student")
name = st.text_input("Student Name")
roll = st.text_input("Roll Number")
dept = st.text_input("Department (e.g., CSE)")
blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
class_name = st.text_input("Class")
mobile = st.text_input("Mobile Number")

if st.button("Add"):
    if name and roll and dept and blood_group and class_name and mobile:
        students.append({"Name": name, "Roll": roll, "Department": dept, "Blood Group": blood_group, "Class": class_name, "Mobile": mobile})
        st.success("Student added")
    else:
        st.warning("Please fill all fields")

st.divider()

# Section 2: View students (table like in app.py)
st.subheader("2.Student List")
if students:
    df = pd.DataFrame(students)
    st.table(df)
else:
    st.info("No students yet. Add one above.")

st.divider()

# Section 3: Delete by roll (kept simple)
st.subheader("3.Delete Student")
if students:
    rolls = [s["Roll"] for s in students]
    roll_to_delete = st.selectbox("Select roll to delete", rolls)
    if st.button("Delete"):
        st.session_state.students = [s for s in students if s["Roll"] != roll_to_delete]
        st.success("Deleted")
else:
    st.caption("Add students before trying to delete.")
