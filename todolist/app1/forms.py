from django import forms
from app1.models import Task
class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','due_date']
        widgets = {'due_date': forms.DateInput(attrs={'type': 'date'})}
