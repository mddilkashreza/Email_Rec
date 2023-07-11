from email.message import EmailMessage

import ssl
import smtplib

email_sender = 'dilkashreza420@gmail.com'
email_password = "Write your password"


email_receiver = 'yotifi9481@mahmul.com'

subject = "Donot forget to smile because your smile is precious"
body = """
When you smile everything will alright no need worry about just have the patient

"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())