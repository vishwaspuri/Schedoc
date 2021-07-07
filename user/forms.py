from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model



CHOICES =(
    (1, "Patient"),
    (2, "Specialist-Physician"),
    (3, "Specialist-Cardiology"),
    (4, "Specialist-Ophthalmology"),
)

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=30, required=False, help_text='Please provide a valid name', label="Full Name")
    email = forms.EmailField(max_length=254, help_text='Please provide a valid email address.', label="Email")
    ph_number = forms.CharField(max_length=10, min_length=10, help_text='Please provide a valid phone number', label="Phone Number")
    type = forms.ChoiceField(choices=CHOICES, label="Are you a?")

    class Meta:
        model = get_user_model()
        fields = ('full_name', 'email', 'ph_number', 'type','password1', 'password2', )