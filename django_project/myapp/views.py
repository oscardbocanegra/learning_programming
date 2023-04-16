from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'index.html')
def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2> " % username)

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html')

def task(request):
    # task = Task.objects.get(tittle = tittle)
    return render(request, 'task.html')