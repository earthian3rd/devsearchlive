from operator import mod
from turtle import title, update
from django.db import models
import uuid  #id에 uuid4 사용하기 위해 임폴트

# Create your models here.
#manytomany
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    # owner =
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) #null은 데이타베이스 / blank는 장고를 위한 빈칸허용
    #freature_image = 
    demo_link = models.CharField(max_length=1000, null=True, blank=True)
    source_link = models.CharField(max_length=1000, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True) #다대다 관계 아래 태그 클래스 불러옴
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.title  #title을 게시물의 대표로 나타냄
    
#1tomany
class Review(models.Model):
    
    VOTE_TYPE = (
        ('up', 'up'),
        ('down', 'down')
    )
    
    # owner =
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')  #1:다 관계 #related_name을 설정해서 views.py에서 쉽게 부를 수 있다.
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.value
    