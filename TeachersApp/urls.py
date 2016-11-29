from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^teachers$', views.getTeachers, name='Teachers'),
    url(r'^teacherform$', views.getTeacherForm, name='TeacherForm'),
	url(r'^addteacher$', views.addTeacher, name='AddTeacher'),
]