from celery import shared_task
from .github_api_call import github_data
from .models import GithubInfo

@shared_task(name= 'github_data_load', ignore_result= True)
def github_data_load():
    github_profile = github_data()
    github_info = GithubInfo.objects.filter(pk= 1)
    if github_info.exists:
        instance = github_info.first()
        instance.name = github_profile['name']
        instance.image = github_profile['image']
        instance.username = github_profile['username']
        instance.bio = github_profile['bio']
        instance.joining_date = github_profile['joining_date']
        instance.repos = github_profile['repos']
        instance.followers = github_profile['followers']
        instance.following = github_profile['following']
        instance.save()
    else:
        github_info = GithubInfo.objects.create(
        name = github_profile['name'],
        image = github_profile['image'],
        username = github_profile['username'],
        bio = github_profile['bio'],
        joining_date = github_profile['joining_date'],
        repos = github_profile['repos'],
        followers = github_profile['followers'],
        following = github_profile['following']
    )
    return github_profile
    