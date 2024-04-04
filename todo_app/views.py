from django.shortcuts import render,redirect
from todo_app.models import todotask

# Create your views here.

def taskfunction(request):
    if request.method=='POST':
        task=request.POST.get('task')
        
        todo=todotask(
            todolist=task,
        )
        todo.save()
        return redirect('homepage')

def homepage(request):
    list=todotask.objects.all()
    return render(request,'home.html',{'view':list})  

def deletefuntion(request,data):
    dele=todotask.objects.get(id=data)
    dele.delete()
    return redirect('homepage')

def editfunction(request,data):
    if request.method=='POST':
        todoedit=todotask.objects.get(id=data)
        todoedit.todolist=request.POST.get('task')
        todoedit.save()
        return redirect('homepage')

def editpage(request,data):
    task=todotask.objects.get(id=data)
    return render(request,'edit.html',{'task':task})
