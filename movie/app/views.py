from urllib import request

from django.shortcuts import render,redirect
from django.views import View

from app.forms import MovieForm

from app.models import Movie


# Create your views here.
# def home(request):
#     return render(request, 'home.html')
# def addmovie(request):
#     return render(request, 'addmovie.html')

class Addmovie(View):
    def get(self,request):
        form_instance = MovieForm()
        context = {'form': form_instance}
        return render(request,'addmovie.html',context)
    def post(self,request):
        form_instance=MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return render(request,'addmovie.html')
class Home(View):
    def get(self,request):
        m=Movie.objects.all()
        context = {'m':m}
        return render(request,'home.html',context)
class Detail(View):
    def get(self,request,i):
        b=Movie.objects.get(id=i)
        context = {'i':b}
        return render(request,'detail.html',context)
class Delete(View):
    def get(self, request,i):
        m=Movie.objects.get(id=i)
        m.delete()
        return redirect('home')
class Edit(View):
    def get(self, request,i):
        m=Movie.objects.get(id=i)
        form_instance = MovieForm(instance=m)
        context = {'form': form_instance}
        return render(request,'edit.html',context)
    def post(self, request,i):
        m=Movie.objects.get(id=i)
        form_instance = MovieForm(request.POST,request.FILES,instance=m)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')


