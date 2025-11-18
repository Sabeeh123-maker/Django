from django.http import HttpResponse
from django.shortcuts import render, redirect


def addition(request):
    if(request.method == 'GET'):
        return render(request, 'addition.html')
    if(request.method == 'POST'):
        n1 = request.POST['num1']
        n2 = request.POST['num2']
        s=int(n1)+int(n2)
        print(s)
        context = {'result':s,'n1':n1,'n2':n2}
        return render(request, 'addition.html',context)
def factorial(request):
    if(request.method == 'GET'):
        return render(request, 'factorial.html')
    if(request.method == 'POST'):
        n= int(request.POST['num'])
        factorial=1
        for i in range(1,n+1):
            if i<=n:
                factorial=factorial*i
        print(factorial)
        context = {'result':factorial,'n':n}
        return render(request, 'factorial.html', context)

def bmi(request):
    if(request.method == 'GET'):
        return render(request, 'bmi.html')
    if(request.method == 'POST'):
        w = float(request.POST['weight'])
        h = float(request.POST['height'])
        d=w/(h**2)
        print(d)
        if(d<18.5):
            p=("Underweight")
        elif(d<25 and d>18.5):
            p=("Normal")
        elif(d<30 and d>25):
            p=("Overweight")
        elif(d<35 and d>30):
            p=("Obese")
        context = {'result':d,'w':w,'h':h,'p':p}
        return render(request, 'bmi.html', context)

