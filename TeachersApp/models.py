from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Teacher(models.Model):
	name = models.CharField(max_length=500)
	university = models.CharField(max_length=500)
	email = models.CharField(max_length=500)
	phone = models.CharField(max_length=500)
