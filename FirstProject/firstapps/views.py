from django.shortcuts import render
from .models import Project


# Create your views here.

def project_index(request):
    project = Project.objects.all()
    context = {
        'project': project
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'projects': project
    }
    return render(request, 'project_index.html', context)
