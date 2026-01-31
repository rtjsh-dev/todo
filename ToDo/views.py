from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def addTask(request):
    # print(request.POST['task'])
    task = request.POST['task']
    Task.objects.create(task=task) 
    # Only variable value here is 'task', so, we will be using that value only
    return redirect('home')