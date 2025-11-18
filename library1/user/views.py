from django.shortcuts import render
from django.views import View
from user.forms import Userform,Loginform



# Create your views here.
#function based

# def register(request):
#     return render(request, 'register.html')
# def login(request):
#     return render(request, 'login.html')

#class based

class Registerview(View):
    def get(self, request):
        form_instance = Userform()
        context = {'form2': form_instance}
        return render(request,'register.html',context)
    def post(self, request):
        form_instance = Userform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            context = {'form2': form_instance}
            return render(request,'register.html',context)
class Loginview(View):
    def get(self, request):
        form_instance = Loginform()
        context = {'form3': form_instance}
        return render(request,'login.html',context)
    def post(self, request):
        form_instance = Loginform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            context = {'form3': form_instance}
            return render(request,'login.html',context)