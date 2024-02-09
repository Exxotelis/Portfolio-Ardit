
from email import message
import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_name = st.text_input("Enter your name ")
    user_email = st.text_input("Your email address ")
    message = st.text_area("Your message ")

    button = st.form_submit_button("Submit")

    if button:
        send_email(user_name, user_email, message)
        st.success("Your message has been sent successfully!")
