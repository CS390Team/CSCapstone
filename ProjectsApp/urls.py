"""ProjectsApp URL Configuration

Created by Harris Christiansen on 10/02/16.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^project/all$', views.getProjects, name='Projects'),
   	url(r'^project/form$', views.getProjectForm, name='ProjectForm'),
    url(r'^project/formsuccess$', views.getProjectFormSuccess, name='ProjectFormSuccess'),
    url(r'^project/remove$', views.removeProject, name='RemoveProject'),
    url(r'^project/update$', views.updateProject, name='UpdateProject'),
    url(r'^project/bookmark$', views.bookmarkProject, name='bookmarkProject'),
    url(r'^project/unbookmark$', views.unbookmarkProject, name='unbookmarkProject'),
    url(r'^project/bookmarks$',views.getBookmarks,name='getBookmarks'),
    url(r'^project$', views.getProject, name='Project'),
]