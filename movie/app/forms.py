from django import forms
from app.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
