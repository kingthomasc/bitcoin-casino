# Create your views here.
from game.models import Game, Bet
from django.shortcuts import render, redirect
import datetime

def game(request, pk):
    game = Game.objects.get(pk=pk)
    return render(request, 'game.html', {'game':game})

def bet(request, pk):
    game = Game.objects.get(pk=pk)
    try:
        bet = Bet.objects.get(game=game, user=request.user)
    except:
        bet = Bet(game=game)
    bet.last_modified = datetime.datetime.now()
    bet.value = request.POST['amount']
    bet.higher = request.POST['higher']
    bet.user = request.user
    bet.save()
    return redirect('/game/' + pk + '/')