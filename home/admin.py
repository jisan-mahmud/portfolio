from django.contrib import admin
from .models import Basic_info, Skill, Project, Contact, GithubInfo

admin.site.register(Basic_info)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(GithubInfo)