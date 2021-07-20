from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponseForbidden
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from user.models import Auth, User, OTP
from appointment.utils.send_email import send_mail
import random


# Create your views here.

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user=user)
                return redirect('appointment:home')
            else:
                return HttpResponseForbidden(
                    "<html><head><title>Login Forbidden</title></head><body><h1>The User is deactivated. Please contact customer service.</h1></body></html>")
        else:
            return redirect(request, 'user/login.html', {
                "is_valid": False,
                "error": "Invalid credentials provided"
            })
    else:
        return render(request, 'user/login.html')


def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            u = Auth(pws=raw_password, em=email)
            u.save()
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            return redirect('appointment:home')
    else:
        form = SignUpForm()
    return render(request, 'user/register.html', {'form': form})

def get_email_and_generate_otp(request):
    if request.method == "POST":
        number = random.randint(1111, 9999)
        email = request.POST["email"]
        try:
            user = User.objects.get(email=email)
            print(0)
            res, _ = send_mail(number, email)
            if res:
                otp = OTP(em=email, otp=number)
                otp.save()
                return redirect("user:otp-verification", email=email)
            else:
                return render(request, "user/otp.html", {"error": ["Couldn't send OTP."]})
        except:
            return render(request, "user/otp.html", {"errors": ["User does not exist"]})
    return render(request, "user/otp.html")


def otp_verification(request, email):
    if request.method == "POST":
        otp = request.POST["otp"]
        latest_otp = OTP.objects.filter(em=email).last()
        if str(otp) == str(latest_otp.otp):
            auth = Auth.objects.get(em=email)
            user = authenticate(username=email, password=auth.pws)
            if user.is_active:
                login(request, user=user)
                print(2)
                return redirect('appointment:home')
            else:
                print(3)
                return render(request, "user/otp_verification.html", {
                    "error": "User is not active.",
                    "email": email
                })
        else:
            return render(request, "user/otp_verification.html", {
                "error": "Incorrect otp",
                "email": email
            })
    return render(request, "user/otp_verification.html", {
        "email": email
    })

@login_required()
def update_user(request):
    user = request.user
    if request.method == "POST":
        new_full_name = request.POST["full_name"]
        new_ph_number = request.POST["ph_number"]
        if str(user.ph_number) != str(new_ph_number) and str(new_ph_number) != "":
            user.ph_number =  new_ph_number
        if str(user.full_name) != str(new_full_name) and str(new_full_name) != "":
            user.full_name =  new_full_name
        user.save()
        return redirect("user:profile")
    return render(request, "user/update_user.html")

@login_required()
def view_doctor(request, doctor_id):
    doctor = User.objects.get(id=doctor_id)
    return render(request, "user/doctor.html", {"doctor":doctor})

@login_required
def my_profile(request):
    user = request.user
    return render(request, 'user/profile.html', {'user': user})


4
