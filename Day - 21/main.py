import streamlit as st

# st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image(r"Day - 21\images\photo.png")

with col2:
    st.title("Partha Pratim Deori")
    content = """
    Hello, I am learning Python. I am from India. I'm 24 years
    old. This is my personal portfolio page which I have created using Streamlit framework. I love programming. 
    Thanks for visiting here. All thanks to Ardit Sulce. He is a good mentor to me. He is very professional.
    I have learn to program in Python by watching his tutorials on Udemy.
    """
    st.info(content)