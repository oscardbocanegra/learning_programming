from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index (request):
    return HttpResponse('Index page')

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2> " % username)

def about(request):
    return HttpResponse ("About")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse (projects, safe=False)

def task(request, tittle):
    task = Task.objects.get(tittle = tittle)
    return HttpResponse ("task: %s" %task.tittle)