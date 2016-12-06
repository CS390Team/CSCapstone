"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO Task 3.5: Add field for company relationship
    post_by = models.CharField(max_length=200, null=True)

    # TODO Task 3.5: Add fields for project qualifications (minimum required: programming language, years of experience, speciality)
    pro_language = models.CharField(max_length=100, null=True)
    years_of_exp = models.PositiveSmallIntegerField(null=True)
    speciality = models.TextField(null=True)

    def __str__(self):
        return self.name