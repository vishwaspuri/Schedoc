from django.views.generic import TemplateView
from user.models import User
# Create your views here.



class LandingPage(TemplateView):
    template_name = 'appointment/landing.html'


class HomePage(TemplateView):
    template_name = 'appointment/home.html'
    model = User
    login_url = '/user/login'