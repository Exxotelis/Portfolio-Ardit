# import config

# import streamlit as st
# import smtplib
# import ssl
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText


# def send_email(user_name, user_email, message):

#     host = config.HOST
#     port = config.PORT
#     username = config.USER
#     password = config.PASS

#     context = ssl.create_default_context()
#     receiver = "exxotelis@gmail.com"
#     subject = f"Message from {user_name}"

#     email_message = MIMEMultipart()
#     email_message["From"] = username
#     email_message["To"] = receiver
#     email_message["Subject"] = subject

#     body = f"""\
#     Message: {message}
#     From: {user_email}
#     """
#     email_message.attach(MIMEText(body, "plain"))

#     try:
#         with smtplib.SMTP_SSL(host, port, context=context) as server:
#             server.login(username, password or "")
#             server.sendmail(username, receiver, email_message.as_string())
#             print("Email sent successfully!")
#     except Exception as e:
#         print(f"An error occurred while sending the email: {e}")
