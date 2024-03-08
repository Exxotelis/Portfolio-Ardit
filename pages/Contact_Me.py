
from email import message
import streamlit as st
from send_email import send_email

st.set_page_config(page_title="Contact Me",
                   page_icon="images/favicon.png", layout="centered")
st.header("Contact Me")

with st.form(key="email_forms"):
    user_name = st.text_input("Enter your name ")
    user_email = st.text_input("Your email address ")
    message = st.text_area("Your message ")

    button = st.form_submit_button("Submit")

    if button:
        send_email(user_name, user_email, message)
        st.success("Your message has been sent successfully!")


col3, empty_col, col4 = st.columns([1.5, 1.5, 1.5])
with col4:
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
