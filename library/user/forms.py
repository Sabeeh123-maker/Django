from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Userform(UserCreationForm):
    #
    # username = forms.CharField()
    # userid = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput)
    # email = forms.EmailField()
    # phone= forms.IntegerField()
    # address = forms.CharField(widget=forms.Textarea)
    # gender_choices = (('male', 'Male'), ('female', 'Female'))
    # gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name']
class Loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)