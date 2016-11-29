from django import forms

class TeacherForm(forms.Form):
    name = forms.CharField(label='Text', max_length=500)
    university = forms.CharField(label='Text', max_length=500)
    email = forms.CharField(label='Text', max_length=500)
    phone = forms.CharField(label='Text', max_length=500)