from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from app1.forms import SignUpForm,LoginForm
from django.contrib import messages
from django.core.mail import send_mail
from app1.models import CustomUser

# Create your views here.
class Homeview(View):
    def get(self, request):
        return render(request, 'home.html')
class Userlogin(View):
    def get(self, request):
        form_instance = LoginForm()
        context = {'form': form_instance}
        return render(request, 'login.html', context)
    def post(self, request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            u=data['username']
            p=data['password']
            user=authenticate(username=u, password=p)
            # if user and user.is_superuser==True:
            if user:
                login(request, user)
                print('admin logged in')
                return redirect('home')
            # elif user and user.role=='student':
            #     login(request, user)
            #     print('student logged in')
            #     return redirect('studenthome')
            # elif user and user.role=='teacher':
            #     login(request, user)
            #     print('teacher logged in')
            #     return redirect('teacherhome')
            else:
                # print('invalid username or password')
                messages.error(request, "Invalid Username or Password!")
                return redirect('login')
class Registerview(View):
    def get(self, request):
        form_instance = SignUpForm()
        context = {'form': form_instance}
        return render(request, 'register.html',context)
    def post(self, request):
        form_instance = SignUpForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.save(commit=False)
            u.is_active=False
            u.save()
            u.generate_otp()
            send_mail(
                "Django Auth OTP",
                u.otp,
                "sabeehtk3@gmail.com",
                [u.email],
                fail_silently=False,
            )
            return redirect('otp')

class Userlogout(View):
    def get(self, request):
        logout(request) #removes the user from current session
        return redirect('home')
# class Adminhome(View):
#     def get(self, request):
#         return render(request, 'admin.html')
# class Teacherhome(View):
#     def get(self, request):
#         return render(request, 'teacher.html')
# class Studenthome(View):
#     def get(self, request):
#         return render(request, 'student.html')
class Otp_verify(View):
    def get(self, request):
        return render(request, 'otp_verify.html')
    def post(self, request):
        o=request.POST['o'] #retrieve the otp send by the user
        u=CustomUser.objects.get(otp=o) #check whether record matching with the entered otp exists
        #if exists then
        u.is_active=True #enabling user to log in
        u.is_verified=True #sets is verified to True
        u.otp=None #clear the otp from table
        u.save() #saves the data
        return redirect('home')
