"""GroupsApp Forms

Created by Naman Patwari on 10/10/2016.
"""
from django import forms
#from tinymce.widgets import TinyMCE

class GroupForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    description = forms.CharField(label='Description', max_length=300)
    #description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label='Description', max_length=300)
    language = forms.CharField(label='Language', max_length=100)
    experience = forms.CharField(label='Experience', max_length=10)
    speciality = forms.CharField(label='Speciality', max_length=3000)

class AddMembersForm(forms.Form):
	email = forms.CharField(label="Email", max_length=100)