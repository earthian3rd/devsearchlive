from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

projectsList = [
                {
                    'id': 1,
                    'title': 'Ecommerce Website',
                    'description': 'Fully functional ecommerce website.',
                    'topRated': True
                    
                },
                {
                    'id': 2,
                    'title': 'Portfolio Website',
                    'description': 'A personal website to write article and display.',
                    'topRated': False
                },
                {
                    'id': 3,
                    'title': 'Social Networt',
                    'description': 'Engoy life together in our planet.',
                    'topRated': True
                }
                    ]

def index(request):
    #name = 'Yellow0721-genius'
    #age = 42 
    context = {'projects': projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObject = None
    
    for i in projectsList:
        if i['id'] == int(pk):
            projectObject = i
    context = {'projects': projectObject}
    return render(request, 'projects/single-project.html', context)
