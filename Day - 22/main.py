import streamlit as st
import pandas

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

content2 = """
    Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv(r"Day - 22\data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Day - 22/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Day - 22/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")