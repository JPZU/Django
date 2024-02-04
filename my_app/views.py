# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def index(request):
    return HttpResponse('<h1>Index Page</h1>')

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>"% username)
    
def about(request):
    return HttpResponse('About')
    
def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def task(request, id):
    task = Task.objects.get(id=id)
    return HttpResponse('Task: %s' % task.title)