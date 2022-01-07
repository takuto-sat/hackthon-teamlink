from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Profile

class SignUpForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(required=False)
    password2 = password1

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('school_number')