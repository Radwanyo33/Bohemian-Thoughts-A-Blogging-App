from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField() # Add email field to the form
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        