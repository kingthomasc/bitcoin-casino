from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    CURRENCIES = (('btc_usd', 'BTC to USD'),
                  ('ltc_usd', 'LTC to USD'),
                  )
    
    startTime = models.DateTimeField()
    endBetTime = models.DateTimeField()
    endTime = models.DateTimeField()
    value = models.DecimalField(max_digits=16, decimal_places=8)
    game_type = models.CharField(max_length="7", choices=CURRENCIES, default='btc_usd')
    
    def get_url(self):
        return "/game/" + self.pk + "/"
    
class Bet(models.Model):
    last_modified = models.DateTimeField()
    user = models.ForeignKey(User)
    value = models.DecimalField(max_digits=16, decimal_places=8)
    game = models.ForeignKey(Game)
    higher = models.BooleanField()