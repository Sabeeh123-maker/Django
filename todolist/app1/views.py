from django.shortcuts import render, redirect
from django.views import View
from app1.forms import TodoForm
from app1.models import Task


# Create your views here.
class TodoView(View):
    def get(self, request):
        form_instance=TodoForm()
        context = {'form':form_instance,'task':Task.objects.all()}
        return render(request,'todo.html',context)
    def post(self,request):
        form_instance = TodoForm(request.POST)
        if form_instance.is_valid():
            print(form_instance.cleaned_data)
            form_instance.save()
            return redirect('home')
        context = {'form':form_instance,'task':Task.objects.all()}
        return render(request,'todo.html',context)
class TodoListView(View):
    def get(self, request):
        t=Task.objects.all()
        context = {'task':t}
        return render(request,'todo.html',context)
class DeleteView(View):
    def get(self, request,i):
        t=Task.objects.get(id=i)
        t.delete()
        return redirect('home')
class EditView(View):
    def get(self, request,i):
        t=Task.objects.get(id=i)
        form_instance=TodoForm(instance=t)
        context = {'form':form_instance}
        return render(request,'edit.html',context)
    def post(self,request,i):
        t=Task.objects.get(id=i)
        form_instance=TodoForm(request.POST,instance=t)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')
class CompleteView(View):
    def get(self, request,i):
        t=Task.objects.get(id=i)
        t.complete=True
        t.save()
        return redirect('home')


