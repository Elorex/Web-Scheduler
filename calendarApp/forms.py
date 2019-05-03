from django import forms
from .models import Events
from django.contrib.auth.models import User

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('title', 'start', 'end', 'description')

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
