from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .forms import TaskForm
from .models import Task
# Create your views here.
def index(request):
    #if the method is POST
    if request.method == 'POST':
        form = TaskForm(request.POST)
        #if the method is valid
        if form.is_valid():
            form.save() #Yes, save
            #redirect to home page
            return HttpResponseRedirect('/')
        else:
            #No, Show error
            return HttpResponseRedirect(form.errors.as_json())
        
    #Get all tasks, limit = 20
    tasks = Task.objects.all().order_by('-created_at')[:20]
    #display 20 tasks
    return render(request, 'tasks.html', {'tasks': tasks})

def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect('/')
    