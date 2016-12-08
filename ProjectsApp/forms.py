from django import forms
from .models import Project

class ProjectForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    description = forms.CharField(label='Description', max_length=300)
    #created_at = models.DateTimeField('date created')
    #updated_at = models.DateTimeField('date updated')

    # TODO Task 3.5: Add field for company relationship
    #company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # TODO Task 3.5: Add fields for project qualifications (minimum required: programming language, years of experience, speciality)
    language = forms.CharField(label='Programming Languages', max_length = 300)
    experience = forms.CharField(label='Years of Experience', max_length = 300)
    speciality = forms.CharField(label='Speciality', max_length = 3000)

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'language', 'experience', 'speciality')

    def clean_name():
        name = self.cleaned_data.get("name")
        if name == self.initial["name"]:
            return name
        try:
            exists = Project.objects.get(name=name)
            raise forms.ValidationError("This project name has already been taken")
        except Project.DoesNotExist:
            return name
        except:
            raise forms.ValidationError("There was an error, please contact us later")

    def clean_description():
        description = self.cleaned_data("description")
        return description

    def clean_language():
        language = self.cleaned_data("language")
        return language

    def clean_experience():
        experience = self.cleaned_data("experience")
        return experience

    def clean_spaciality():
        speciality = self.cleaned_data("speciality")
        return speciality
