from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player
from .forms import PlayerForm
# Create your views here.
def index(req):
    players = Player.objects.all()
    return render(req,'rmapp/index.html',{'players': players })

def buy(req):
    form = PlayerForm()
    if req.method == "POST":
        form = PlayerForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('rmapp:index')
    return render(req,'rmapp/buy.html',{'form':form})

def sell(req,id):
    player = Player.objects.get(pk=id)
    if req.method=='POST':
        player.delete()
        return redirect('rmapp:index')
    return render(req,'rmapp/sell.html',{'player':player})

def update(req,id):
    player = Player.objects.get(pk=id)
    form = PlayerForm(instance=player)
    if req.method=='POST':
        form = PlayerForm(req.POST,instance=player)
        if form.is_valid():
            form.save()
        return redirect('rmapp:index')
    return render(req,'rmapp/update.html',{'form' : form, 'player' : player})