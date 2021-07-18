from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from appointment.utils.send_email import send_mail
import random
from user.models import User

@api_view(["POST"])
def send_otp(request):
    print(0)
    print(request)
    number = random.randint(1111, 9999)
    email = request.POST["email"]
    print(email)
    try:
        user = User.objects.get(email=email)
    except:
        return Response({
            "status": False,
            "Error": "User does not exist"
        }, status = status.HTTP_403_FORBIDDEN)
    res, _ = send_mail(number, email)
    if res:
        return Response({
            "status": True,
            "otp": number
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            "status": False,
            "Error": "Could not send email"
        }, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

