from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from user.models import User
from appointment.models import Appointment
from django.contrib.auth.decorators import login_required
from user.utils import user_type
import datetime
from appointment.utils.time_slots import TIME_SLOTS
# Create your views here.

@login_required
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
@login_required()
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

@login_required()
def create_appointment(request, date, doctor_id, timeslot):
    print(date)
    print(doctor_id)
    print(TIME_SLOTS[int(timeslot)])
    doctor = User.objects.get(id=doctor_id)
    if request.method == "POST":
        user = request.user
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        time = TIME_SLOTS[int(timeslot)]
        dt = datetime.datetime.combine(time=time, date=date)
        reason_for_appointment = request.POST["description"]
        appointment = Appointment()
        appointment.user = user
        appointment.doctor = doctor
        appointment.time = dt
        appointment.reason_for_appointment = reason_for_appointment
        appointment.save()
        return redirect("appointment:home")
    return render(request, "appointment/create_appointment.html", {
        "doctor": doctor,
        "timeslot":timeslot,
        "time": TIME_SLOTS[int(timeslot)],
        "date": date,
    })

@login_required()
def home(request):
    user = request.user
    context = dict()
    context["user"] = user
    context["appointments"] = Appointment.objects.filter(user=user, time__gte=datetime.datetime.now())
    return render(request, "appointment/home.html", context=context)

@login_required()
def appointment_history(request):
    context = dict()
    context["user"] = request.user
    if request.user.type is 1:
        context["appointments"] = Appointment.objects.filter(user=request.user, time__lte=datetime.datetime.now())
    else:
        context["appointments"] = Appointment.objects.filter(doctor=request.user, time__lte=datetime.datetime.now())
    return render(request, "appointment/appointment_history.html", context=context)

class LandingPage(TemplateView):
    template_name = 'appointment/landing.html'