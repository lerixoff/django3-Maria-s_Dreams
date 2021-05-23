from django.shortcuts import render
from .models import Project

def project(request):
    return render(request, 'project.html')

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

