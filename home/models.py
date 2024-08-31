from django.db import models

class SingletonModel(models.Model):
    class Meta:
        abstract = True
    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class Basic_info(SingletonModel):
    name = models.CharField(max_length= 60)
    image = models.ImageField(upload_to= 'image/')
    about = models.TextField()
    email = models.EmailField(max_length= 100)
    linkedin = models.URLField(max_length= 50)
    github = models.URLField(max_length= 50)
    facebook = models.URLField(max_length= 50)

    def __str__(self) -> str:
        return self.name
    

class Skill(models.Model):
    user = models.ForeignKey(Basic_info, on_delete=models.CASCADE)
    technology_name = models.CharField(max_length= 100)
    technology_icon = models.CharField(max_length= 100)
    color_code = models.CharField(max_length=20 ,blank= True)

    def __str__(self) -> str:
        return self.technology_name
    
class Project(models.Model):
    user = models.ForeignKey(Basic_info, on_delete= models.CASCADE)
    title = models.TextField(max_length= 100)
    image = models.ImageField(upload_to= 'image/project/')
    description = models.TextField()
    live_link = models.URLField(max_length= 100, blank= True)
    github_repo_link = models.URLField(max_length= 100, blank= True)

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    email = models.EmailField()
    message = models.TextField()

class GithubInfo(models.Model):
    name = models.CharField(max_length= 100)
    image = models.ImageField(upload_to= 'image/github')
    username = models.CharField(max_length= 50)
    bio = models.CharField(max_length= 100, blank= True, null= True)
    joining_date = models.CharField(max_length= 50)
    repos = models.IntegerField()
    followers = models.IntegerField()
    following = models.IntegerField()