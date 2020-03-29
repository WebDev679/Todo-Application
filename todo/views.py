from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
# Create your views here.

def home(request):
    tasks = Task.objects.all()
    return render(request, 'todo/home.html', {'tasks':tasks})


def add_task(request):
    if request.method == 'POST':
        task = Task()
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']
        task.save()
        return redirect('home')

def delete_task(request):
    if request.method == 'POST':
        tasks = Task.objects.all()
        tasks_deleted = []
        for task in tasks:
            delete = request.POST.get(str(task.id), None)
            print (delete)
            if delete is not None:
                tasks_deleted.append(task)
        for task in tasks_deleted:
            task.delete()
        return redirect('home')
