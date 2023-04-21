# This script is sending an email

# import elements
import e_mail_data
from email.message import EmailMessage  # for e-mail service
import smtplib  # necessary to connect with gmail

e_mail_sender = e_mail_data.e_mail_address
e_mail_password = e_mail_data.password
e_mail_receiver = e_mail_data.e_mail_receiver

subject = "Test email by python"
body = """
This is my first program for sending email using python script
"""

em = EmailMessage()
em['From'] = e_mail_sender
em['To'] = e_mail_receiver
em['Subject'] = subject
em.set_content(body)

# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.login(e_mail_sender, e_mail_password)
# server.sendmail(e_mail_sender, e_mail_receiver, em.as_string())

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(e_mail_sender, e_mail_password)
    server.sendmail(e_mail_sender, e_mail_receiver, em.as_string())
