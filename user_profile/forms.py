'''
Created on May 21, 2013

@author: Thomas
'''
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField()
    re_email = forms.CharField()
    address = forms.CharField()
    phone_number = forms.CharField()