"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models
from CompaniesApp.models import Company

class Project(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=10000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
	
	language = models.CharField(max_length=100)
	experience = models.CharField(max_length=10)
	speciality = models.CharField(max_length=10000)

	post_by = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.name