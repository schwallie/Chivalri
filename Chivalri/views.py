# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:38:49 2013

@author: Chase
"""

from django.shortcuts import render
from models import Businessid,Cuisineid,Dealdb,Ratingsdb,Userid,Userlogin,Uservisitdb,Waitressid
from django import forms
from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
  
from django.contrib.auth.decorators import login_required

@login_required  
def expand(request):
    userid = Userid.objects.filter(name__contains="Schwalbach")
    return render(request,'usercp/expand.html',{'userid':userid})
    
def home(request):
    if  request.user.is_authenticated():
        return expand(request)
    else:
        return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })