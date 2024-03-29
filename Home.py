import os
import streamlit as st
import pandas as pd


st.set_page_config(page_title="Exxotelis",
                   page_icon="images/favicon.png", layout="wide")


col1, col2 = st.columns(2)

with col1:
    st.image("images/Exxotelis.png", width=400)

with col2:
    st.title("Exxotelis")
    content = st.write("""
        About Me
        Hey there! I'm Lefteris Kapsalidis, a London-based
        professional with a background in both management and
        software engineering. I'm passionate about
        leveraging technology to drive innovation and
        create positive change in the world.

        Professional Journey
        I started my career in the construction industry,
        where I gained valuable experience in leadership and
        team management. However, my true passion lies in
        software engineering, which led me to pursue a
        Skills Software Engineering Bootcamp at HyperionDev.
        Here, I'm diving deep into full-stack development and
        honing my skills in Python, JavaScript, HTML, CSS, and more.

        What I Bring to the Table
        I thrive in dynamic environments and love tackling complex
        challenges. Whether it's developing innovative solutions for
        fintech or collaborating with talented teams,
        I'm dedicated to making a meaningful impact.

        Let's Connect
        I'm always open to new opportunities and collaborations.
        Whether you're a fellow tech enthusiast or a prospective employer,
        I'd love to connect. Feel free to reach out via email or
        connect with me on LinkedIn.
        """)

    st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <div style="font-size: 24px;">
        <a href="#" class="fab fa-facebook"></a>
        <a href="#" class="fab fa-twitter"></a>
        <a href="https://github.com/Exxotelis" class="fab fa-github"></a>
        <a href="https://www.linkedin.com/in/lefteris-kapsalidis-8360412a6/" class="fab fa-linkedin"></a>
        <a href="#" class="fab fa-youtube"></a>
    </div>
    """, unsafe_allow_html=True)
st.write("")

# Create another set of columns below the first set
content2 = """
    Below you will find some of the apps I have built in Python.
    Feel free to contact me!
    """
st.info(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")
images_dir = "./images"  # Directory where images are stored

# Iterate over the first 10 rows for column 3
for index, row in df[:10].iterrows():
    with col3:
        st.header(row["title"])
        st.write(row["description"])  # Access description from data.csv
        # Construct full image path
        image_path = os.path.join(images_dir, row["image"])
        st.image(image_path, width=300)
        st.write(f"[Source Code]({row['url']})")


# Define the image path and the corresponding hyperlink URL
image_path = "images/1.png"
hyperlink_url = "https://realm-analysis.streamlit.app/"

# Display the image with a clickable link
st.markdown(f"[![image]({image_path})]({hyperlink_url})")


# Iterate over the remaining rows for column 4
for index, row in df[10:].iterrows():
    with col4:
        st.header(row["title"])  # Move this line inside col4 context manager

        st.write(row["description"])
        # Construct full image path
        image_path = os.path.join(images_dir, row["image"])
        st.image(image_path, width=300)
        st.write(f"[Source Code]({row['url']})")
st.divider()
st.pydeck_chart()  # Placeholder for map
