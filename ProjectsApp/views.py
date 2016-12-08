"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.shortcuts import render

from . import models
from . import forms
from datetime import datetime
from GroupsApp.models import Group

def getProjects(request):
	projects_list = models.Project.objects.all()
	group_list = Group.objects.all()
	if request.user.is_student:
		recommend = []
		for project in projects_list:
			score=0

			pro_lan_list = []
			pro_lan = []
			for char in project.language:
				if char == ',':
					pro_lan_list.append(pro_lan)
					pro_lan = []
				else:
					pro_lan.append(char)
			pro_lan_list.append(pro_lan)

			pro_spe_list = []
			pro_spe = []
			for char in project.speciality:
				if char == ',':
					pro_spe_list.append(pro_spe)
					pro_spe = []
				else:
					pro_spe.append(char)
			pro_spe_list.append(pro_spe)

			for group in group_list:
				print "Statement"
				group_lan_list = []
				group_lan = []
				for char in group.languages:
					if char == ',':
						group_lan_list.append(group_lan)
						group_lan = []
					else:
						group_lan.append(char)
				group_lan_list.append(group_lan)

				group_spe_list = []
				group_spe = []
				for char in group.speciality:
					if char == ',':
						group_spe_list.append(group_spe)
						group_spe = []
					else:
						group_spe.append(char)
				group_spe_list.append(group_spe)
				
				if (group.members.filter(email__exact=request.user.email)):
					for p_lan in pro_lan_list:
						for g_lan in group_lan_list:
							if p_lan == g_lan:
								score = score + 1
					if float(project.experience) <= float(group.experience):
						score = score + 1
					for p_spe in pro_spe_list:
						for g_spe in group_spe_list:
							if p_spe == g_spe:
								score = score + 1
				if score > 0:
					pair = []
					pair.append(project)
					pair.append(group)
					recommend.append(pair) 
					print group.name

		return render(request, 'projects.html', {'projects' : projects_list,'recommend' : recommend})

	return render(request, 'projects.html', {
        'projects': projects_list,
    })

def getProject(request):
	if request.user.is_authenticated():
		in_company_name = request.GET.get('name', 'None')
		in_company = models.Company.objects.get(name__exact=in_company_name)
		in_project_name = request.GET.get('project', 'None')
		in_project = in_company.project_set.get(name__exact=in_project_name)
		#is_member = group
		context = {
			'company' : in_company,
			'project' : in_project,
		}
		return render(request, 'project.html', context)
	return render(request, 'autherror.html')

def getProjectForm(request):
	if request.user.is_authenticated():
		in_name = request.GET.get('name', 'None')
		#in_company = models.Company.objects.get(name__exact=in_name)
		context = {
			'company' : in_name,
			'page_name' : 'Create',
			'button_value' : 'Submit',
			'project_id' : -1
		}
		return render(request, 'projectform.html', context)
	# render error page if user is not logged in
	return render(request, 'autherror.html')

def getProjectFormSuccess(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = forms.ProjectForm(request.POST, request.FILES)
			if form.is_valid():
				in_name = request.GET.get('name', 'None')
				in_company = models.Company.objects.get(name__exact=in_name)
				
				if request.GET.get('action') == 'Update':
					if (request.GET.get('id') != -1):
						in_project = models.Project.objects.get(id=request.GET.get('id'))
						in_project.name = form.cleaned_data['name']
						in_project.description=form.cleaned_data['description']
						in_project.experience=experience=form.cleaned_data['experience']
						in_project.speciality=speciality=form.cleaned_data['speciality']
						in_project.updated_at=str(datetime.now())
						in_project.save()
					
				elif request.GET.get('action') == 'Create':
					if in_company.project_set.filter(name__exact=form.cleaned_data['name']).exists():
						return render(request, 'projectform.html', {'error' : 'Error: That project name already exists at this company!'})
					new_project = models.Project(name=form.cleaned_data['name'], 
                                             description=form.cleaned_data['description'],
                                             language=form.cleaned_data['language'],
                                             experience=form.cleaned_data['experience'],
                                             speciality=form.cleaned_data['speciality'],
                                             company=in_company,
                                             post_by=request.user.email
                                             )
					new_project.save()
					in_company.project_set.add(new_project)

				is_member = in_company.members.filter(email__exact=request.user.email)
				context = {
					'company' : in_company,
					'userIsMember' : is_member,
				}
				return render(request, 'company.html', context)
			else:
				return render(request, 'projectform.html', {'error' : 'Undefined Error!'})
		else:
			form = forms.ProjectForm()
			return render(request, 'projectform.html')
	#render error page if user is not logged in
	return render(request, 'autherror.html')

def removeProject(request):
	if request.user.is_authenticated():
		in_company_name = request.GET.get('name', 'None')
		in_company = models.Company.objects.get(name__exact=in_company_name)
		in_project_name = request.GET.get('project', 'None')
		in_project = in_company.project_set.get(name__exact=in_project_name)
		in_project.delete()
		is_member = in_company.members.filter(email__exact=request.user.email)
		context = {
			'company' : in_company,
			'userIsMember' : is_member,
		}
		return render(request, 'company.html', context)
	return render(request, 'autherror.html')

def updateProject(request):
	in_project_name = request.GET.get('project', 'None')
	in_project = models.Project.objects.get(name__exact=in_project_name)
	in_company_name = request.GET.get('name', 'None')
	in_company = models.Company.objects.get(name__exact=in_company_name)
	form=forms.UpdateForm(request.POST or None, instance=in_project)
	if form.is_valid():
		form.save()
		messange.success(request, 'Success, project was saved!')

	context = {
		'form' : form,
		'page_name' : 'Update',
		'button_value' : 'Update',
		'links' : ['logout'],
		'company': in_company,
		'project_id' : in_project.id
	}
	return render(request, 'projectform.html', context)





