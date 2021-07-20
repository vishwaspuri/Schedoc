from mailjet_rest import Client
import os

def send_mail(otp, email):
    html_content = '<strong>Your OTP is ' + str(otp) + '.</strong>'
    api_key = ''
    api_secret = ''
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
      'Messages': [
        {
          "From": {
            "Email": "vishwaspuri09@gmail.com",
            "Name": "Vishwas"
          },
          "To": [
            {
              "Email": email,
              "Name": "Vishwas"
            }
          ],
          "Subject": "Schedoc OTP",
          "HTMLPart": html_content,
          "CustomID": "AppGettingStartedTest"
        }
      ]
    }
    result = mailjet.send.create(data=data)
    return True, "sent"

# import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

# def send_mail(otp, email):
#     html_content = '<strong>Your OTP is '+str(otp)+'.</strong>'
#     message = Mail(
#         from_email='vishwaspuri09@gmail.com',
#         to_emails=email,
#         subject='Schedoc OTP',
#         html_content=html_content,
#     )
#
#     try:
#         sg = SendGridAPIClient('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')
#         response = sg.send(message)
#         return True, response.status_code
#     except Exception as e:
#         return False, e.message