from django.shortcuts import render
from django.views import View
from employees.forms import EmpForm
from employees.models import Employee


# Create your views here.
class Addview(View):
    def get(self,request):
        form_instance = EmpForm()
        context={'form':form_instance}
        return render(request,'employee.html',context)
    def post(self,request):
        form_instance = EmpForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            form_instance.save()
            context={'form':form_instance}
        return render(request,'employee.html',context)
