from django import forms
from django.contrib.auth.forms import UserCreationForm
from app1.models import CustomUser


class SignUpForm(UserCreationForm):
    role_choices=(('student','Student'),('teacher','Teacher'))
    role=forms.ChoiceField(choices=role_choices)
    class Meta:
        model = CustomUser
        fields = ('username','password1','password2', 'email','first_name', 'last_name','phone','role')
    #UserCreationForm is used for password encryption and password verification
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)