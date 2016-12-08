"""GroupsApp Views
Created by Naman Patwari on 10/10/2016.
"""
from django.shortcuts import render

from . import models
from . import forms
from .models import MyUser

def getGroups(request):
    if request.user.is_authenticated():
        users_list = models.MyUser.objects.all()
        for user in users_list:
            print("%s %s") %(user.email, user.get_full_name())

        email = request.user.email
        is_student = request.user.is_student
        is_professor = request.user.is_professor
        is_engineer = request.user.is_engineer

        groups_list = models.Group.objects.all()
        context = {
            'groups' : groups_list,
        }
        return render(request, 'groups.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        is_member = in_group.members.filter(email__exact=request.user.email)
        context = {
            'group' : in_group,
            'userIsMember': is_member,
        }
        return render(request, 'group.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroupForm(request):
    if request.user.is_authenticated():
        return render(request, 'groupform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroupFormSuccess(request):
    print("this is called")
    if request.user.is_authenticated():
        if request.method == 'POST':
            print("POST")
            form = forms.GroupForm(request.POST)
            if form.is_valid():
                print("form valid")
                if models.Group.objects.filter(name__exact=form.cleaned_data['name']).exists():
                    return render(request, 'groupform.html', {'error' : 'Error: That Group name already exists!'})
                description=form.cleaned_data['description']
                print("description")
                print(description)
                new_group = models.Group(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
                new_group.save()
                context = {
                    'name' : form.cleaned_data['name'],
                }
                return render(request, 'groupformsuccess.html', context)
        else:
            print("form not valid")
            form = forms.GroupForm()
        return render(request, 'groupform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def joinGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        in_group.members.add(request.user)
        in_group.save();
        request.user.group_set.add(in_group)
        request.user.save()
        context = {
            'group' : in_group,
            'userIsMember': True,
        }
        return render(request, 'group.html', context)
    return render(request, 'autherror.html')
    
def unjoinGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        in_group.members.remove(request.user)
        in_group.save();
        request.user.group_set.remove(in_group)
        request.user.save()
        context = {
            'group' : in_group,
            'userIsMember': False,
        }
        return render(request, 'group.html', context)
    return render(request, 'autherror.html')

def getAddMembersForm(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        context = {
            'group' : in_group,
            'userIsMember': True,
        }
        return render(request, 'addmemberform.html', context)
    return render(request, 'autherror.html')

def addMembers(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.AddMembersForm(request.POST)
            if form.is_valid():
                # find user
                # warn if user is not found
                in_user_email = form.cleaned_data['email']
                print(in_user_email)
                if not models.MyUser.objects.filter(email__exact=in_user_email).exists():
                    return render(request, 'addmemberform.html', {'error' : 'Error: The user does not exist'})
                
                in_user = models.MyUser.objects.get(email__exact=in_user_email)
                print("user found")
                
                # find group
                in_group_name = request.GET.get('name', "None")
                # in_group_name = "Bridges International" # TODO: get group name
                print(in_group_name)
                in_group = models.Group.objects.get(name__exact=in_group_name)

                # print out all members of the group
                print("All members:")
                for member in in_group.members.all():
                    print(member.email)
                
                # check if user already in the group
                if in_group.members.filter(email__exact=in_user_email):
                    return render(request, 'addmemberform.html', {'error' : 'Error: The user is already a member'})
                
                # check if user is a student
                if not in_user.is_student:
                    return render(request, 'addmemberform.html', {'error' : 'Error: The user is not a student'})
                
                # add user to group
                in_group.members.add(in_user)
                in_group.save();
                in_user.group_set.add(in_group)
                in_user.save()
                
                context = {
                    'group' : in_group,
                    'userIsMember': True,
                }
            return render(request, 'group.html', context)
        else:
            form = forms.GroupForm()
        return render(request, 'groupform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')
    