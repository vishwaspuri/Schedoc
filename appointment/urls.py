from django.urls import path
from appointment import views

urlpatterns=[
    path('', views.LandingPage.as_view(), name="land"),
    path('home', views.HomePage.as_view(), name="home"),
    path('find_doctor', views.find_doctor, name="find-doctor"),
    path('select_slot/<str:date>/<str:doctor_id>/', views.timeslots, name="select-slots")
]