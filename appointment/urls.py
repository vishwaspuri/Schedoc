from django.urls import path
from appointment import views

urlpatterns=[
    path('', views.LandingPage.as_view(), name="land"),
    path('home', views.home, name="home"),
    path('find_doctor', views.find_doctor, name="find-doctor"),
    path('select_slot/<str:date>/<str:doctor_id>', views.timeslots, name="select-slots"),
    path('create_appointment/<str:date>/<str:doctor_id>/<str:timeslot>', views.create_appointment, name="create-appointment"),
    path('appointment_history', views.appointment_history, name="appointment-history"),
    path('my_patients', views.patient_list, name="my-patients"),
    path('view_appointment/<int:appointment_id>', views.view_appointment, name="view-appointment")
]