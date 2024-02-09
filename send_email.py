from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl


# def send_email(user_email, message):
#     host = "smtp.gmail.com"
#     port = 465

#     username = "exxotelis@gmail.com"
#     password = "mxib gvto ilvq sidu"

#     context = ssl.create_default_context()
#     receiver = "exxotelis@gmail.com"

#     message = """\
#     Subject: Hello!

#     This is a test email sent using Python.
#     """

#     with smtplib.SMTP_SSL(host, port, context=context) as server:
#         server.login(username, password)
#         server.sendmail(username, receiver, message)


def send_email(user_name, user_email, message):
    host = "smtp.gmail.com"
    port = 465
    username = "exxotelis@gmail.com"
    password = "mxib gvto ilvq sidu"

    context = ssl.create_default_context()
    receiver = "exxotelis@gmail.com"

    # Replace "user_name" with "user_email"
    subject = f"Message from {user_name}"

    # Create a multipart message
    email_message = MIMEMultipart()
    email_message["From"] = username
    email_message["To"] = receiver
    email_message["Subject"] = subject

    # Add body to email
    body = f"""\
    Message: {message}
    From: {user_email}
    """
    email_message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, email_message.as_string())
