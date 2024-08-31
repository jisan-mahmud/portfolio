from django.shortcuts import render
from django.views import View
from .models import Basic_info, Skill, Project
from django.shortcuts import redirect
from .forms import ContactForm
from django.contrib import messages
from django.urls import reverse
from .models import GithubInfo

class Home(View):
    def get(self, request, *args, **kwargs):
        basic_info = Basic_info.objects.get(pk=1)
        skills = Skill.objects.all()
        projects = Project.objects.all()
        context = {
            'basic_info': basic_info,
            'skills': skills,
            'projects': projects,
        }
        github_info = GithubInfo.objects.filter(pk=1)
        if github_info.exists:
            context['github_profile'] = github_info.first()
        
        return render(request, 'home/index.html', context = context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'message sending success...')
        else:
            messages.error(request, 'something went wrong try again...')

        url = reverse('home') + '?#contact'
        return redirect(url)