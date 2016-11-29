from django.shortcuts import render

from . import models
# from . import forms
# Create your views here.
def getEngineers(request):
    return render(request, 'engineers.html')