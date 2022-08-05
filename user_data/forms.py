from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user_data.models import Thesis


class ThesisForm(forms.ModelForm):

    class Meta:
        model = Thesis
        fields = ('cleaver',)
        widgets = {
            'cleaver': forms.Select(choices=Thesis.CHOICES)
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
