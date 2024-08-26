from django.shortcuts import render
from django.views import View
from .models import Basic_info, Skill, Project
from django.urls import reverse

class Home(View):
    def get(self, request, *args, **kwargs):
        basic_info = Basic_info.objects.get(pk=1)
        skills = Skill.objects.all()
        projects = Project.objects.all()
        context = {
            'basic_info': basic_info,
            'skills': skills,
            'projects': projects
        }
        return render(request, 'home/index.html', context = context)