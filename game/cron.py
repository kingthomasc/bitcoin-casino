'''
Created on May 9, 2013

@author: Thomas
'''
from django_cron import CronJobBase, Schedule
from game.models import Game
import datetime
from decimal import Decimal
from urllib2 import urlopen 
import json

class UpdateGames(CronJobBase):
    RUN_EVERY_MINS = 1
    
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'games.update_games'
    
    def do(self):
        now = datetime.datetime.now()
        prev = now - datetime.timedelta(minutes=1)
        games = Game.objects.filter(endTime__range=[prev, now])
        for game in games:
            if game.value == Decimal(0):
                current_value = Decimal(json.loads(urlopen("https://btc-e.com/api/2/" + game.game_type + "/ticker"))["ticker"]["last"])
                game.value = current_value
                game.save()
                