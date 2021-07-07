from django.urls import path
from appointment import views

urlpatterns=[
    path('', views.LandingPage.as_view(), name="land"),
    path('home', views.HomePage.as_view(), name="home"),
]