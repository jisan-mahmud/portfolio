from django.shortcuts import render
from django.views import View
from .models import Basic_info, Skill, Project
from .github_api_call import github_info
from django.shortcuts import redirect

class Home(View):
    def get(self, request, *args, **kwargs):
        basic_info = Basic_info.objects.get(pk=1)
        skills = Skill.objects.all()
        projects = Project.objects.all()
        github_profile = github_info()
        context = {
            'basic_info': basic_info,
            'skills': skills,
            'projects': projects,
        }
        if github_info != 0:
            context['github_profile'] = github_info
        return render(request, 'home/index.html', context = context)
    
    def post(self, request):
        print(request.POST)
        return redirect('home')