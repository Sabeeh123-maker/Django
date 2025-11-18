from django.shortcuts import render
from django.views import View
from app1.forms import Studentform
from app1.models import Student
# Create your views here.
class Addview(View):
    def get(self, request):
        form_instance = Studentform()
        context = {'form': form_instance}
        return render(request, 'addview.html', context)
    def post(self, request):
        form_instance = Studentform(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            form_instance.save()
            return render(request, 'addview.html')
class Home(View):
    def get(self, request):
        return render(request, 'homeview.html')


