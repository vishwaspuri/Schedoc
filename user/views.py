from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponseForbidden
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from user.models import Auth
from django.views.decorators.http import require_http_methods

# Create your views here.

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password  = request.POST['password']
        user = authenticate(username = email, password= password)
        if user is not None:
            if user.is_active:
                login(request, user=user)
                return redirect('appointment:home')
            else:
                return HttpResponseForbidden("<html><head><title>Login Forbidden</title></head><body><h1>The User is deactivated. Please contact customer service.</h1></body></html>")
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

def otp_login(request):
    if request.method=="POST":
        email = request.POST["email"]
        auth = Auth.objects.get(email=email)
        password = auth.pws
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
    return render(request, "user/otp.html")

@login_required
def my_profile(request):
    user = request.user
    return render(request, 'user/profile.html', {'user': user})

