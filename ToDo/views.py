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
    task = get_object_or_404(Task, pk=pk)
    task.is_Completed = True
    task.save(update_fields=["is_Completed"])
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_Completed = False
    task.save(update_fields=["is_Completed"])
    return redirect('home')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        new_task = request.POST['task']
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        context ={
            'task':task
            }
        return render(request, 'edit_task.html', context)
    
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')