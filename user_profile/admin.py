'''
Created on May 7, 2013

@author: Thomas
'''
from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib.sites.models import Site
from user_profile.models import UserProfile

# admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)