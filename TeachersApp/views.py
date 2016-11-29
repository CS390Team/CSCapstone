from django.shortcuts import render

from . import models
from . import forms

# Create your views here.
def getTeachers(request):
	teacher_list = models.Teacher.objects.all()
	context = {
		'teachers' : teacher_list
	}
	return render(request, 'teachers.html', context)

def getTeacherForm(request):
	return render(request, 'teacherForm.html')

def addTeacher(request):
	if request.method == 'POST':
		form = forms.TeacherForm(request.POST)
		if form.is_valid():
			new_teacher = models.Teacher(name=form.cleaned_data['name'], university=form.cleaned_data['university'], email=form.cleaned_data['email'], phone=form.cleaned_data['phone'])
			new_teacher.save()
			teacher_list = models.Teacher.objects.all()
			context = {
				'teachers' : teacher_list,
			}
			return render(request, 'teachers.html', context)
		else:
			form = forms.CommentForm()
	return render(request, 'teachers.html')