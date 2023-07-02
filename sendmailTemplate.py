# To use this program, install the below python module 
# pip install psycopg2

#!/usr/bin/env python

import psycopg2
import smtplib

from email.mime.text import MIMEText

def get_email_addresses():
    """Retrieve email addresses from the database."""
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )
    cursor = conn.cursor()
    
    # Retrieve email addresses from the table
    cursor.execute("SELECT email FROM students where name in ('Abhishek Sagar', 'Shivani Nigam')" )
    email_records = cursor.fetchall()
    
    email_addresses = [record[0] for record in email_records]
    
    cursor.close()
    conn.close()
    
    return email_addresses

def send_email(sender_email, sender_password, recipient_email, subject, message):
    """Send an email."""
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.close()
        print("Email sent successfully to {}".format(recipient_email))
    except Exception as e:
        print("Failed to send email to {}: {}".format(recipient_email, str(e)))

# Example usage
email_addresses = get_email_addresses()

sender_email = "csepracticals@gmail.com"
sender_password = "kcryywrjdlwjbxzj"
subject = "Test Email Automation ...."
message = "This is a test email."

for recipient_email in email_addresses:
    send_email(sender_email, sender_password, recipient_email, subject, message)
