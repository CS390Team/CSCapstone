"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.shortcuts import render

from . import models
from . import forms

def getProjects(request):
	projects_list = models.Project.objects.all()
	return render(request, 'projects.html', {
        'projects': projects_list,
    })

def getProject(request):
	project_list = models.Project.objects.filter(post_by=request.user.email)
	print project_list
	context = {
		'project' : project_list
	}
	return render(request, 'project.html', context)

def getProjectForm(request):
	return render(request, 'projectForm.html')

def addProject(request):
	if request.user.is_authenticated():
		form=forms.ProjectForm(request.POST)
		if form.is_valid():
			new_project=models.Project(name=form.cleaned_data['name'],
							  	   	   description=form.cleaned_data['description'],
							  	   	   pro_language=form.cleaned_data['language'],
							  	   	   years_of_exp=form.cleaned_data['exp'],
							  	   	   speciality=form.cleaned_data['speciality'],
							  	   	   post_by=request.user.email)
			new_project.save()
			project_list = models.Project.objects.filter(post_by=request.user.email)
			context = {
				'project' : project_list
			}
			return render(request, 'project.html', context)
		else:
			return render(request, 'projects.html', {'error': 'Undefined Error!'})

