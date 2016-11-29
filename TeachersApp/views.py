from django.shortcuts import render

from . import models

# Create your views here.
def getTeachers(request):
	return render(request, 'teachers.html')