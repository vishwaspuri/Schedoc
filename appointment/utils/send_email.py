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
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        return True, response.status_code
    except Exception as e:
        return False, e.message