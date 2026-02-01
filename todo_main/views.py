from django.shortcuts import render
from ToDo.models import Task

def home(request):
    tasks = Task.objects.filter(is_Completed=False).order_by('updated_at')
    completed_tasks = Task.objects.filter(is_Completed=True)
    # print(completed_tasks)
    # print(list(tasks))
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        }
    return render(request, 'home.html', context, )