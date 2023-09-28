from django.shortcuts import redirect, get_object_or_404, render
from .models import Task
from django.http import HttpResponse

# Create your views here.
def addTask(request):
    if request.method=='POST':
        task = request.POST['task']
        Task.objects.create(task=task)
        return redirect('home')
    
def mark_as_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, task_id):
    get_task = get_object_or_404(Task, id=task_id)
    if request.method=='POST':
        updated_task = request.POST['updated_task']
        get_task.task = updated_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request, "edit_task.html", context)

def delete_task(request, task_id):
    get_task = get_object_or_404(Task, id=task_id)
    get_task.delete()
    return redirect('home')
    
