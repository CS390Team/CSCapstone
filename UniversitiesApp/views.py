"""
UniversitiesApp Views

Created by Jacob Dunbar on 11/5/2016.
"""
from django.shortcuts import render

from . import models
from . import forms
from AuthenticationApp.models import MyUser, Professor, Student

def getUniversities(request):
    if request.user.is_authenticated():
        universities_list = models.University.objects.all()
        context = {
        'universities' : universities_list,
        }
        return render(request, 'universities.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getUniversity(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_name)
        is_member = in_university.members.filter(email__exact=request.user.email)

        context = {
        'university' : in_university,
        'userIsMember': is_member,
        'userIsProfessor' : request.user.is_professor
        }
        return render(request, 'university.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getUniversityForm(request):
    if request.user.is_authenticated():
        return render(request, 'universityform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getUniversityFormSuccess(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.UniversityForm(request.POST, request.FILES)
            if form.is_valid():
                if models.University.objects.filter(name__exact=form.cleaned_data['name']).exists():
                    return render(request, 'universityform.html', {'error' : 'Error: That university name already exists!'})
                    new_university = models.University(name=form.cleaned_data['name'],
                       photo=request.FILES['photo'],
                       description=form.cleaned_data['description'],
                       website=form.cleaned_data['website'])
                    new_university.save()
                    context = {
                    'name' : form.cleaned_data['name'],
                    }
                    return render(request, 'universityformsuccess.html', context)
                else:
                   return render(request, 'universityform.html', {'error' : 'Error: Photo upload failed!'})
            else:
               form = forms.UniversityForm()
               return render(request, 'universityform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def joinUniversity(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_name)

        if request.user.university_set.count() != 0:
            context = {
                'university' : in_university,
                'userIsMember': False,
                'userIsProfessor' : request.user.is_professor,
                'error' : 'Error: You already joined another university!'
            }
            return render(request, 'university.html', context)
        
        in_university.members.add(request.user)
        in_university.save();
        request.user.university_set.add(in_university)
        request.user.save()

        context = {
            'university' : in_university,
            'userIsMember': True,
            'userIsProfessor' : request.user.is_professor
        }
        return render(request, 'university.html', context)
    else:
        return render(request, 'autherror.html')

def unjoinUniversity(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_name)
        in_university.members.remove(request.user)
        in_university.save();
        request.user.university_set.remove(in_university)
        request.user.save()

        context = {
        'university' : in_university,
        'userIsMember': False,
        }
        return render(request, 'university.html', context)
    else:
        return render(request, 'autherror.html')

def getCourse(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_university_name)
        in_course_tag = request.GET.get('course', 'None')
        in_course = in_university.course_set.get(tag__exact=in_course_tag)
        is_member = in_course.members.filter(email__exact=request.user.email)
        context = {
        'university' : in_university,
        'course' : in_course,
        'userIsProfessor' : request.user.is_professor,
        }
        return render(request, 'course.html', context)
    return render(request, 'autherror.html')

def getCourses(request):
    if request.user.is_authenticated():
        courses = models.Course.objects.all()
        context = {
        'courses' : courses,
        }
        return render(request, 'courses.html', context)
        return render(request, 'autherror.html')

def courseForm(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_university_name)
        context = {
        'university': in_university,
        }
        return render(request, 'courseform.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def addCourse(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = forms.CourseForm(request.POST)
			if form.is_valid():
				in_university_name = request.GET.get('name', 'None')
				in_university = models.University.objects.get(name__exact=in_university_name)
				print(in_university.name)
				if in_university.course_set.filter(tag__exact=form.cleaned_data['tag']).exists():
					return render(request, 'courseform.html', {'error' : 'Error: That course tag already exists at this university!'})
				new_course = models.Course(tag=form.cleaned_data['tag'],
										   name=form.cleaned_data['name'],
										   description=form.cleaned_data['description'],
										   university=in_university,
										   professor=models.Professor.objects.get(user_id=request.user.id)
										   )
				new_course.save()
				in_university.course_set.add(new_course)
				is_member = in_university.members.filter(email__exact=request.user.email)
				context = {
					'university' : in_university,
					'userIsMember': is_member,
					'userIsProfessor' : request.user.is_professor
				}
				return render(request, 'university.html', context)
			else:
				return render(request, 'courseform.html', {'error' : 'Undefined Error!'})
		else:
			form = forms.CourseForm()
			return render(request, 'courseform.html')
		# render error page if user is not logged in
	return render(request, 'autherror.html')

def removeCourse(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', 'None')
        print(in_university_name)
        in_university = models.University.objects.get(name__exact=in_university_name)
        in_course_tag = request.GET.get('course', 'None')
        in_course = in_university.course_set.get(tag__exact=in_course_tag)
        in_course.delete()
        is_member = in_university.members.filter(email__exact=request.user.email)
        context = {
        'university' : in_university,
        'userIsMember' : is_member,
        'userIsProfessor' : request.user.is_professor
        }
        return render(request, 'university.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def addStudentsForm(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', "None")
        in_university = models.University.objects.get(name__exact=in_university_name)
        in_name = request.GET.get('course', 'None')
        in_course = models.Course.objects.get(tag__exact=in_name)
        context = {
        'university' : in_university,
        'course' : in_course,
        }
        return render(request, 'addstudentsform.html', context)
    else:
        return render(request, 'autherror.html')


def addStudents(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.AddStudentsForm(request.POST)
            if form.is_valid():
                in_university_name = request.GET.get('name', 'None')
                in_university = models.University.objects.get(name__exact=in_university_name)
                in_course_tag = request.GET.get('course', 'None')
                in_course = in_university.course_set.get(tag__exact=in_course_tag)

                in_user_email = form.cleaned_data['email']
                print(in_user_email)

                if in_course.members.filter(email__exact=in_user_email).exists():
                    return render(request, 'addstudentsform.html', {'error' : 'Error: The student is already in this course!'})

                in_user = models.MyUser.objects.get(email__exact=in_user_email)
                in_course.members.add(in_user)
                in_course.save()
                request.user.course_set.add(in_course)
                request.user.save()
                context = {'university' : in_university,
                'course' : in_course,
                'userIsProfessor' : request.user.is_professor,
                }
                return render(request, 'course.html', context)
            else:
                return render(request, 'addstudentsform.html', {'error' : 'Undefined Error!'})
        else:
            form = forms.AddStudentsForm()
            return render(request, 'addstudentsform.html')
    return render(request, 'autherror.html')

def removeStudent(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', "None")
        in_university = models.University.objects.get(name__exact=in_university_name)
        in_email = request.GET.get('email', 'None')
        in_user = models.MyUser.objects.get(email__exact=in_email)
        in_course_tag = request.GET.get('course', 'None')
        in_course = in_university.course_set.get(tag__exact=in_course_tag)
        in_course.members.remove(in_user)
        in_course.save();
        in_user.course_set.remove(in_course)
        in_user.save()
        context = {
          'university' : in_university,
          'course' : in_course,
          'userIsProfessor': request.user.is_professor,
        }
        return render(request, 'course.html', context)
    return render(request, 'autherror.html')

