# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'Django course!!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'zulua'
    return render(request, 'about.html', {
        'username': username
    })

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>"% username)
    
    
def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def task(request):
    # task = Task.objects.get(title=title)
    task = Task.objects.all()
    return render(request, 'task.html', {
        'tasks': task
    })