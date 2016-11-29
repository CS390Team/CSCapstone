from django import forms

class EngineerForm(forms.Form):
    name=forms.CharField(max_length=50)
    alma_mater=forms.CharField(max_length=100)
    about=forms.CharField(max_length=200)
    contact_info=forms.CharField(max_length=15)