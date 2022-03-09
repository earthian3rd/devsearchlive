from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

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
    projects = Project.objects.all  #데이타베이스 전체를 불러와서 변수에 한꺼번에 일단 넣음
    context = {'projects': projects}  #딕셔너리 형태로 데이타베이스 변수를 지정하고 다른 변수에 넣음
    return render(request, 'projects/projects.html', context) #변수를 웹사이트로 보냄

def project(request, pk):
    projectObj = Project.objects.get(id=pk) #데이타베이스중 겟으로 일부 불러옴
    tags = projectObj.tags.all()  #이미 위에서 id값에 해당하는 딕셔너리 다 가져옴 그중에서 tags뽑음
    #reviews = projectObj.review_set.all() #일단 왜인지 모르나 class인 Review를 소문자 review_set으로 쓰고 모두 불러온다
    reviews = projectObj.reviews.all() #models.py에 있는 related_name의 값으로 쉽게 불러온다
    context = {'projects': projectObj, 'tags': tags, 'reviews': reviews}
    return render(request, 'projects/single-project.html', context)
