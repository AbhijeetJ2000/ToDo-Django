from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    pendingTasks = Task.objects.filter(is_completed=False).order_by('updated_at')
    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    context = {
        'pendingTasks': pendingTasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'home.html', context)


