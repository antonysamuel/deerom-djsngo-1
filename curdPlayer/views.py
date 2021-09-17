from django.shortcuts import redirect, render
from django.views import View
from .models import Player,Game
from .forms import AddPlayerForm
# Create your views here.

class HomeView(View):
    def get(self,req):
        player_data  = Player.objects.all()
        return render(req, 'home.html',{'playerData': player_data})


class AddPlayer(View):
    def get(self,req):
        frm = AddPlayerForm
        return render(req,'addPlayer.html',{'form':frm})
    def post(self,req):
        fm = AddPlayerForm(req.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        return render(req,'addPlayer.html',{'from': fm})


class DeletePlayer(View):
    def post(self,req):
        data = req.POST
        id = data.get('id')
        player = Player.objects.get(id = id)
        if player:
            player.delete()
        return redirect('/')

class UpdatePlayer(View):
    def get(self,req,id):
        player = Player.objects.get(id=id)
        frm = AddPlayerForm(instance=player)
        return render(req,'updatePlayer.html',{'form':frm})
    def post(self,req,id):
        player = Player.objects.get(id=id)
        frm = AddPlayerForm(req.POST,instance=player)
        if frm.is_valid():
            frm.save()
            return redirect('/')
        return render(req,'updatePlayer.html',{'form':frm})