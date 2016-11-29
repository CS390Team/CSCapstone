from django.shortcuts import render

from . import models
from . import forms

# Create your views here.
def getEngineers(request):
    engineers_list = models.Engineer.objects.all()
    context = {
        'engineers' : engineers_list,
    }
    return render(request, 'engineers.html', context)

def getEngineerForm(request):
    return render(request, 'engineerForm.html')

def addEngineer(request):
    if request.method == 'POST':
        form = forms.EngineerForm(request.POST)
        if form.is_valid():
            new_engineer = models.Engineer(name=form.cleaned_data['name'], alma_mater=form.cleaned_data['alma_mater'], about=form.cleaned_data['about'], contact_info=form.cleaned_data['contact_info'])
            new_engineer.save()
            engineers_list = models.Engineer.objects.all()
            context = {
                'engineers' : engineers_list,
            }
            return render(request, 'engineers.html', context)
        else:
            form = forms.EngineerForm()
    return render(request, 'engineers.html')