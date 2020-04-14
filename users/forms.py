from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
      primary_email = forms.EmailField()
      recovery_email = forms.EmailField()
      #date_of_birth = forms.DateField()

      class Meta:
          model = User
          fields = ['username','primary_email','recovery_email','password1','password2']


