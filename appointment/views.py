from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class LandingPage(TemplateView):
    template_name = 'appointment/landing.html'

class HomePage(TemplateView):
    template_name = 'appointment/home.html'