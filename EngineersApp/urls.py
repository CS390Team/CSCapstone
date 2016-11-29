from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^engineers$', views.getEngineers, name='Engineers'),
]