'''
Created on May 9, 2013

@author: Thomas
'''
from django.contrib import admin
from game.models import Game, Bet

class GameAdmin(admin.ModelAdmin):
    pass

class BetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Game, GameAdmin)
admin.site.register(Bet, BetAdmin)