# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:38:49 2013

@author: Chase
"""

from django.shortcuts import render
from django.http import HttpResponse
from models import Businessid,Cuisineid,Dealdb,Ratingsdb,Userid,Userlogin,Uservisitdb,Waitressid
    
def expand(request):
    userid = Userid.objects.filter(name__contains="Schwalbach")
    return render(request,'usercp/expand.html',{'userid':userid})