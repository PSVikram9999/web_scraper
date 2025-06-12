
import smtplib
from email.mime.text import MIMEText

def send_email(product_name, current_price, target_price, email_to):
    msg = MIMEText(f"Price drop alert!\n\n{product_name}\nNow: {current_price}\nTarget: {target_price}")
    msg['Subject'] = 'Price Alert!'
    msg['From'] = 'your_email@example.com'
    msg['To'] = email_to

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login('your_email@example.com', 'your_app_password')
        server.send_message(msg)
