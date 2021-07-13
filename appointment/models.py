from django.db import models
from django.contrib.auth import get_user_model
from user.utils import user
# Create your models here.

class Appointment(models.Model):
    doctor = models.ForeignKey(to=get_user_model(),validators=[user.validate_doctor], related_name='patient_appointments', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(to=get_user_model(), related_name='doctor_appointments', on_delete=models.CASCADE)
    time = models.DateTimeField()
    prescription = models.TextField(max_length=256, null=True)
    reason_for_appointment = models.TextField(max_length=256, null=True)
    payment = models.FloatField(default=0)
    payment_paid = models.BooleanField(default=False)
    feedback = models.TextField(max_length=256, null=True)