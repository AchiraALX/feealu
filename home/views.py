from hashlib import new
from re import template
from sqlite3 import Date
from django.shortcuts import render
from django .http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


from home.models import comments


def comm(request):
    comment = comments.objects.all().order_by('-date').values()
    template = loader.get_template('comm.html')
    context = {
        'comments': comment
    }
    
    return HttpResponse(template.render(context, request))

def addcomment(request):
    comment = request.POST['comment']
    author = request.POST['author']
    date = Date.today()

    comment = comments(content=comment, author=author, date=date)
    comment.save()


    return HttpResponseRedirect(reverse('comm'))



def home(requet):
    template = loader.get_template('home.html')

    return HttpResponse(template.render({}, requet))

def about(request):
    template = loader.get_template('about.html')

    return HttpResponse(template.render({}, request))
# Create your views here.
