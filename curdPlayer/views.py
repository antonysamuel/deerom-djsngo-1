from django.shortcuts import redirect, render
from django.views import View
from .models import Player,Game
from .forms import AddPlayerForm
# Create your views here.

class HomeView(View):
    def get(self,req):
        player_data  = Player.objects.all()
        data = []
        for player in player_data:
            game = Game.objects.filter(user = player)
            score = 0
            for g in game:
                score += g.score
            df = {
                'player' : player,
                'game' : len(game),
                'score' : score
            }
            data.append(df)
        data = sorted(data,key=lambda i: i['score'],reverse=True)
        return render(req, 'home.html',{'playerData': data})


class AddPlayer(View):
    def get(self,req):
        frm = AddPlayerForm
        return render(req,'addPlayer.html',{'form':frm})
    def post(self,req):
        game = req.POST.get('game','')
        score = req.POST.get('score','')
        print(f"Score: {score}\nGame: {game}")
        print(req.POST)
        player = Player(player_name = req.POST['player_name'],player_email =req.POST['player_email'],country=req.POST['country'])
        ply = Player.objects.filter(player_email = player.player_email)
        if len(ply) == 0:
            player.save()
            game = Game(user=player,game=game,score=score)
            game.save()
            print(player)
            print("Adding player")
            return redirect('/')
        else:
            game = Game(user=ply[0],game=game,score=score)
            game.save()
            print(ply)
            return redirect('/')
        # fm = AddPlayerForm(req.POST)
        # if fm.is_valid():
        #     fm.save()
        #     return redirect('/')
        return render(req,'addPlayer.html')


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
        games = Game.objects.filter(user=player)
        frm = AddPlayerForm(instance=player)
        return render(req,'updatePlayer.html',{'form':frm,'games':games})
    def post(self,req,id):
        player = Player.objects.get(id=id)
        frm = AddPlayerForm(req.POST,instance=player)
        if frm.is_valid():
            frm.save()
            return redirect('/')
        return render(req,'updatePlayer.html',{'form':frm})