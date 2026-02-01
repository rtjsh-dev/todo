from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.
def addTask(request):
    # print(request.POST['task'])
    task = request.POST['task']
    Task.objects.create(task=task) 
    # Only variable value here is 'task', so, we will be using that value only
    return redirect('home')

def mark_as_done(request, pk):
    # print(pk)
    task = get_object_or_404(Task, pk=pk)
    task.is_Completed =True
    task.save()
    return redirect('home')