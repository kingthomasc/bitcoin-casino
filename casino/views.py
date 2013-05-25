'''
Created on May 9, 2013

@author: Thomas
'''
from django.shortcuts import render
import datetime
from game.models import Game, Bet

def home(request):
    now = datetime.datetime.now();
    active_games = Game.objects.filter(startTime__lt=now, endBetTime__gt=now)
    context = {}
    context['active_games'] = active_games
    if request.user.is_authenticated():
        my_bets = Bet.objects.filter(user=request.user, game__endTime__gt=now)
        my_games = []
        for bet in my_bets:
            my_games.append(bet.game)
        context['my_games'] = my_games
    return render(request, 'home.html', context)