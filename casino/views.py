'''
Created on May 9, 2013

@author: Thomas
'''
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})