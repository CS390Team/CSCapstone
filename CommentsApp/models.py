from __future__ import unicode_literals

from django.db import models
from GroupsApp.models import Group

class Comment(models.Model):
    time = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=500)
    post_by = models.CharField(max_length=500,null=True)
    name = models.CharField(max_length=500,null=True)
    group = models.ForeignKey(Group,null=True)