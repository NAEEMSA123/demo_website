
import streamlit as st




name = st.text_input("Enter Your Name")
fname = st.text_input("Enter Your Father Name")

add = st.text_area("Enter Your Address")

class1 = st.selectbox("Enter your Class", [1,2,3, 4,5])

button = st.button("Done")


if button :
    st.markdown(f"""
                \n
Name: {name}
\n
Father Name: {fname}
\n
Address : {add}
\n
class1: {class1}
""")




