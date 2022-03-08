from django.urls import path
from . import views   #views의 def 사용하기 위해

urlpatterns = [
    path('', views.index),
    path('project/<str:pk>', views.project),
]
