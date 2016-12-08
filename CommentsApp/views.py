from django.shortcuts import render

from . import models
from . import forms
from GroupsApp.models import Group

def getComments(request):
    comments_list = models.Comment.objects.all()
    context = {
        'comments' : comments_list,
    }
    return render(request, 'comments.html', context)

def getCommentForm(request):
    group = request.GET.get('group','None')
    context = {
           'group' : group,
    }
    return render(request, 'commentForm.html', context)

def addComment(request):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            new_comment = models.Comment(comment=form.cleaned_data['comment'],
                                         post_by = request.user.email,
                                         name = request.user.get_full_name())
            new_comment.save()
            group_name = request.GET.get('group','None')
            group = Group.objects.get(name__exact=group_name)
            group.comment_set.add(new_comment)

            context = {
                'comments' : group.comment_set.all(),
                'group':group,
            }
            return render(request, 'group.html', context)
        else:
            form = forms.CommentForm()
    return render(request, 'group.html')

def removeComment(request):
    if request.user.is_authenticated():
        c_id = request.GET.get('id', 'None')
        group_name = request.GET.get('group','None')
        print "c_id",c_id
        group = Group.objects.get(name__exact=group_name)
        comment = group.comment_set.get(id = int(c_id))
        comment.delete()
        context = {
                'comments' : group.comment_set.all(),
                'group':group
        }
        return render(request, 'group.html',context)
    # render error page if user is not logged in    
    return render(request, 'group.html')