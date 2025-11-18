from django.shortcuts import render
from django.views import View
from app1.forms import Additionform,Factorialform,Bmiform,Signupform




class Addition(View):
    def get(self, request):
        form_instance = Additionform()
        context = {'form': form_instance}
        return render(request, 'addition.html',context)
    def post(self, request):
        #creating form object using submitted data
        form_instance = Additionform(request.POST)
        #check whether data is submitted or not
        if form_instance.is_valid():
            #process the data after validation
            data = form_instance.cleaned_data
            print(data)
            n1 = data['num1']
            n2 = data['num2']
            s=n1+n2
            context = {'result':s,'form': form_instance}
            return render(request, 'addition.html',context)


class Factorial(View):
    def get(self, request):
        form_instance = Factorialform()
        context = {'form': form_instance}
        return render(request, 'factorial.html',context)
    def post(self, request):
        form_instance = Factorialform(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            print(data)
            n=data['num']
            fact=1
            for i in range(1,n+1):
                fact=fact*i
            print(fact)
            context = {'result':fact,'form': form_instance}
            return render(request, 'factorial.html',context)

class Bmi(View):
    def get(self, request):
        form_instance = Bmiform()
        context = {'form': form_instance}
        return render(request, 'bmi.html',context)
    def post(self, request):
        form_instance = Bmiform(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            print(data)
            h=data['height']
            w=data['weight']
            bmi=w/(h/100)**2
            print(bmi)
            if (bmi < 18.5):
                p = ("Underweight")
            elif (bmi < 25 and bmi > 18.5):
                p = ("Normal")
            elif (bmi < 30 and bmi > 25):
                p = ("Overweight")
            elif (bmi < 35 and bmi > 30):
                p = ("Obese")
            context = {'result':bmi,'form': form_instance,'p':p}
            return render(request, 'bmi.html',context)

class Signup(View):
    def get(self, request):
        form_instance = Signupform()
        context = {'form': form_instance}
        return render(request, 'signup.html',context)
    def post(self, request):
        form_instance = Signupform(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            print(data)
            context = {'result':data,'form': form_instance}
            return render(request, 'signup.html',context)
