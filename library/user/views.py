from django.contrib.auth import logout,login,authenticate
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
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
            form_instance.save()
            return redirect('home')

class Loginview(View):
    def get(self, request):
        form_instance = Loginform()
        context = {'form3': form_instance}
        return render(request,'login.html',context)
    def post(self, request):
        form_instance = Loginform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data #fetches data after validation
            u=data['username']#retrieves username from cleaned data
            p=data['password']#retrieves username from cleaned data
            user=authenticate(username=u,password=p)#calls authenticate to verify if user exists
                                                    #if user exists then it returns to the user object
                                                    #else none
            if user:#if user exists
                login(request,user)  #add the user into current session
                return redirect('home')
            else: #if not exists
                messages.error(request, "Invalid Username or Password!")
                return redirect('user:login')

class Logoutview(View):
    def get(self, request):
        logout(request)
        return redirect('home')