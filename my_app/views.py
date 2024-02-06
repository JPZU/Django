# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>"% username)
    
    
def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html')

def task(request):
    # task = Task.objects.get(title=title)
    return render(request, 'task.html')