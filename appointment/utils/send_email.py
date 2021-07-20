import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail(otp, email):
    html_content = '<strong>Your OTP is '+str(otp)+'.</strong>'
    message = Mail(
        from_email='vishwaspuri09@gmail.com',
        to_emails=email,
        subject='Schedoc OTP',
        html_content=html_content,
    )

    try:
        sg = SendGridAPIClient('')
        response = sg.send(message)
        return True, response.status_code
    except Exception as e:
        return False, e.message