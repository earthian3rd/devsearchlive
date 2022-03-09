from django.contrib import admin
from .models import Project, Review, Tag
# Register your models here.

admin.site.register(Project) #관리자 페이지에 추가
admin.site.register(Review)
admin.site.register(Tag)