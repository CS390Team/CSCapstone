from __future__ import unicode_literals

from django.db import models

class Engineer(models.Model):
    name=models.CharField(max_length=50)
    about=models.CharField(max_length=200)
    contact_info=models.CharField(max_length=15)