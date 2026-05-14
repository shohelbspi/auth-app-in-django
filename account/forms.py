from django import forms 

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class SingUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

        labels = {'email':'Email'}

class UserProfileEditForm(UserChangeForm):
    password = None

    class Meta:
        model=User
        fields = ['email','first_name','last_name']

