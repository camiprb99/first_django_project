from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

class ProfileRegisterForm(forms.ModelForm):
    lastname = forms.CharField(label='Nume')
    firstname =forms.CharField(label='Prenume')
    role = forms.ChoiceField(label = 'Rol', choices=[(x, x) for x in ['Student', 'Profesor']])

    class Meta:
        model = Profile
        fields = ['lastname', 'firstname', 'role']