from dataclasses import fields
from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'  #모델에서 만든 Project의 db를 모두 사용하겠다.