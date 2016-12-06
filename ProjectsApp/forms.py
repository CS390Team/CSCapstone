from django import forms

class ProjectForm(forms.Form):
	name = forms.CharField(label='name', widget=forms.TextInput, required=True)
	description = forms.CharField(label='description', widget=forms.Textarea, required=True)
	pro_language = forms.CharField(label='language', widget=forms.TextInput, required=True)
	years_of_exp = forms.CharField(label='exp', widget=forms.TextInput, required=True)
	speciality = forms.CharField(label='speciality', widget=forms.Textarea, required=True)