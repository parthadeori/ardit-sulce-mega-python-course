import streamlit as st
import pandas

# Set webpage layout to wide
st.set_page_config(layout="wide")

# Add a header and some other text
st.header("The Best Company")
st.write("""
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ut ante pellentesque, 
            laoreet diam vel, bibendum lorem. Pellentesque vel diam tempor, varius quam in, placerat 
            dolor. Integer consequat purus vitae metus ornare, in facilisis justo imperdiet. Vestibulum 
            interdum feugiat tellus, quis placerat libero varius et. Phasellus id justo sem. Nulla 
            facilisi. Etiam id sodales nibh, non lobortis ex. Nunc at augue congue, mollis quam sit 
            amet, tempor eros. Suspendisse eu luctus enim. Phasellus a fringilla tellus, non iaculis ante. 
            Pellentesque imperdiet vestibulum nisl, at laoreet nisi convallis eu. Proin laoreet, leo non 
            auctor pulvinar, nulla nisi porttitor nisl, sit amet rhoncus sem ligula et augue. Quisque 
            blandit tincidunt erat, eu dignissim felis consequat at. 
        """)
st.header("Our Team")

# Prepare the columns
col1, col2, col3 = st.columns(3)

# Make a dataframe with the company members
df = pandas.read_csv(r"streamlit-mini-project\data.csv")

# Add content to the first column
with col1:
    # Iterate over only the first four rows
    for index, row in df[:4].iterrows():
        # Add members first and last names
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("streamlit-mini-project/images/" + row["image"])

# Add content to the second column
with col2:
    # Iterate over rows 4 to 7
    for index, row in df[4:8].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("streamlit-mini-project/images/" + row["image"])

# Add content to the third column
with col3:
    # Iterate over rows 4 to 7
    for index, row in df[8:].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("streamlit-mini-project/images/" + row["image"])