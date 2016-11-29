from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^engineers$', views.getEngineers, name='Engineers'),
    url(r'^engineerform$', views.getEngineerForm, name='EngineerForm'),
    url(r'^addengineer$', views.addEngineer, name='AddEngineer'),
]