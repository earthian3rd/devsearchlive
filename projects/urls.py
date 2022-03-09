from django.urls import path
from . import views   #views의 def 사용하기 위해

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<str:pk>', views.project, name='single-project'), #name값을 사용해서 url을 고정해서 줄수 있어 편하다. html페이지에서 href="{% url 'name값' project.id %}"
]
