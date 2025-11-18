from django.http import HttpResponse
from django.shortcuts import render
#
# def home(request):
#     return HttpResponse("Hello, welcome to django home page.")
# def index(request):
#     return HttpResponse("Hello, welcome to index page.")
# def new(request):
#     return HttpResponse("Hello,its new page.write with fresh mind")
def index(request):
    context = {'name':'sabeeh','age':22}
    return render(request, 'index.html', context)
def home(request):
    return render(request, 'home.html')
