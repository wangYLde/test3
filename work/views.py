# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request,'login.html')




def index_view(request):
    return render(request,'index.html')


def nav_view(request):
    return render(request,'nav.html')