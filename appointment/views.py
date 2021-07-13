from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from user.models import User
from appointment.models import Appointment
from user.utils import user_type
import datetime
from appointment.utils.time_slots import TIME_SLOTS
# Create your views here.


def find_doctor(request):
    if request.method == "POST":
        appointment_date = request.POST["appointmentDate"]
        speciality = request.POST["speciality"]
        doctors = User.objects.filter(type=int(speciality))
        speciality = user_type.USER[int(speciality)]
        return render(request, 'appointment/find_doctor.html', {
            'speciality': speciality,
            'appointment_date': appointment_date,
            'resultPresent': True,
            'doctors': doctors
        })
    else:
        return render(request, 'appointment/find_doctor.html', {
            "resultPresent": False
        })

def timeslots(request, date, doctor_id):
    doctor = User.objects.get(id=doctor_id)
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    slots = []
    for i in range(0,40):
        dt = datetime.datetime.combine(time=TIME_SLOTS[i+1], date=date) #Date and time of slot
        if Appointment.objects.filter(doctor=doctor, time=dt).exists():
            slots.append({
                'time': dt.time(),
                'isFull': True
            })
        else:
            slots.append({
                'time': dt.time(),
                'isFull': False
            })
    return render(request, 'appointment/select_slot.html',{
        'doctor': doctor,
        'date':date,
        'slots': slots
    })

class LandingPage(TemplateView):
    template_name = 'appointment/landing.html'


class HomePage(TemplateView):
    template_name = 'appointment/home.html'
    model = User
    login_url = '/user/login'