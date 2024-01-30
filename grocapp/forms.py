from django import forms
from django.contrib.auth.forms import UserCreationForm

class customUserCreatonForm(UserCreationForm):
    
    name = forms.CharField(max_length=200,)
    email = forms.EmailField()
