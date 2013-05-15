# Create your views here.
from game.models import Game
from django.shortcuts import render

def game(request, pk):
    game = Game.objects.get(pk=pk)
    return render(request, 'game.html', {})

def bet(request):
    pass