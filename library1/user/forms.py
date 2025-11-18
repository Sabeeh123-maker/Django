from django import forms

class Userform(forms.Form):

    username = forms.CharField()
    userid = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    phone= forms.IntegerField()
    address = forms.CharField(widget=forms.Textarea)
    gender_choices = (('male', 'Male'), ('female', 'Female'))
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)

class Loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)