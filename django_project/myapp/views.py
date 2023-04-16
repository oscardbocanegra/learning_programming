from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render

# Create your views here.
def index (request):
    title = 'Django course!!'
    return render(request, 'index.html', {
        'title' : title
    })

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2> " % username)

def about(request):
    username = 'Oscar Bocanegra'
    return render(request, 'about.html',{
        'username' : username
    })

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects' : projects
    })

def task(request):
    # task = Task.objects.get(tittle = tittle)
    tasks = Task.objects.all()
    return render(request, 'task.html', {
        'tasks': tasks
    })
    