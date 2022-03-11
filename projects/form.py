from dataclasses import fields
from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):  #model에서 제공하는 form을 사용하겠고 내용은 Project의 것이다.
    class Meta:
        model = Project
        fields = '__all__'  #모델에서 만든 Project의 db를 모두 사용하겠다.
        exclude = ['vote_total','vote_ratio'] #모두 포함한 후 그 중에 제외