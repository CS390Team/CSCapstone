"""GroupsApp Models

Created by Naman Patwari on 10/10/2016.
"""
from django.db import models
from AuthenticationApp.models import MyUser
from ProjectsApp.models import Project

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    members = models.ManyToManyField(MyUser)
    project = models.ForeignKey(Project,default=None,null=True)

    languages = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=20, null=True)
    speciality = models.CharField(max_length=200, null=True)

    is_project = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name