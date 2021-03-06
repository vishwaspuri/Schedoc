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
    path('view_appointment/<int:appointment_id>', views.view_appointment, name="view-appointment"),
    path('delete_appointment/<int:appointment_id>', views.delete_appointment, name="delete-appointment"),
    path('my_patients/<str:patient_id>', views.view_patient, name="view-patient"),
    path('appointment_feedback/<int:appointment_id>', views.give_appointment_feedback, name="appointment-feedback"),
    path('appointment_prescription/<int:appointment_id>', views.give_appointment_prescription, name="appointment-prescription"),
    path('select_updated_slot/<int:appointment_id>', views.select_slot_for_update, name="select-updated-slot"),
    path('update_slot/<int:appointment_id>/<int:timeslot>', views.update_appointment_slot, name="update-timeslot"),
    path('payment_made/<int:appointment_id>', views.payment_made, name="payment-made"),
    path('add_payment/<int:appointment_id>', views.add_payment, name="add-payment")
]