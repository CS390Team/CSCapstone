"""AuthenticationApp Views

Created by Naman Patwari on 10/4/2016.
"""

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from UniversitiesApp.models import University

from .forms import LoginForm, RegisterForm, UpdateForm
from . import models
from .models import MyUser, Student, Professor, Engineer

# Auth Views

def auth_login(request):
	form = LoginForm(request.POST or None)
	next_url = request.GET.get('next')
	if next_url is None:
		next_url = "/"
	if form.is_valid():
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		user = authenticate(email=email, password=password)
		if user is not None:
			messages.success(request, 'Success! Welcome, '+(user.first_name or ""))
			login(request, user)
			return HttpResponseRedirect(next_url)
		else:
			messages.warning(request, 'Invalid username or password.')
			
	context = {
		"form": form,
		"page_name" : "Login",
		"button_value" : "Login",
		"links" : ["register"],
	}
	return render(request, 'auth_form.html', context)

def auth_logout(request):
	logout(request)
	messages.success(request, 'Success, you are now logged out')
	return render(request, 'index.html')

def auth_register(request):
	# if request.user.is_authenticated():
		# return HttpResponseRedirect("/")
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		email=form.cleaned_data['email']
		first_name=form.cleaned_data['firstname']
		last_name=form.cleaned_data['lastname']

		identity = form.cleaned_data['identity']

		new_user = MyUser.objects.create_user(email=form.cleaned_data['email'], 
			password=form.cleaned_data["password2"], 
			first_name=form.cleaned_data['firstname'], 
			last_name=form.cleaned_data['lastname'],
            is_student = form.cleaned_data['student'],
            is_professor = form.cleaned_data['professor'],
            is_engineer = form.cleaned_data['engineer'],
            university = form.cleaned_data['university'])
                       
		new_user.save()
                u_list = University.objects.all()
                curUniv = u_list[int(new_user.univ)-2]
		#Also registering students
                if new_user.is_student == True:	
		    new_student = Student(user = new_user,university = curUniv)
		    new_student.save()
                elif new_user.is_professor == True:
                    new_professor = Professor(user = new_user,university = curUniv)
                    new_professor.save()
                elif new_user.is_engineer == True:
                    new_engineer = Engineer(user = new_user,university = curUniv)
                    new_engineer.save()
                #print new_student.university
		login(request, new_user);

		messages.success(request, 'Success! Your account was created.')
		return render(request, 'index.html')

	context = {
		"form": form,
		"page_name" : "Register",
		"button_value" : "Register",
		"links" : ["login"],
	}
	return render(request, 'auth_form.html', context)

@login_required
def update_profile(request):
	form = UpdateForm(request.POST or None, instance=request.user)
	if form.is_valid():
		identity = form.cleaned_data['identity']
		if (identity == "student"):
			request.user.is_student = True
			request.user.is_professor = False
			request.user.is_engineer = False
		elif (identity == "professor"):
			request.user.is_student = False
			request.user.is_professor = True
			request.user.is_engineer = False
		elif (identity == "engineer"):
			request.user.is_student = False
			request.user.is_professor = False
			request.user.is_engineer = True

		request.user.save()
		form.save()
		messages.success(request, 'Success, your profile was saved!')

	context = {
		"form": form,
		"page_name" : "Update",
		"button_value" : "Update",
		"links" : ["logout"],
	}
	return render(request, 'auth_form.html', context)

def getStudents(request):
	if request.user.is_authenticated():
		students = models.Student.objects.all()
		for item in students:
			print(item.user.email)
		context = {
			'students' : students,
		}
		return render(request, 'students.html', context)
	return render(request, 'autherror.html')
