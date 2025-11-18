from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def first(request):
    return HttpResponse("first page")
def second(request):
    return HttpResponse("second page")
def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')