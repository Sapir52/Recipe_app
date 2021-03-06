from django.contrib.auth.models import User
from django import forms
from .models import Feedback

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = []