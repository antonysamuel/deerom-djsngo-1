from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Player(models.Model):
    id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=150)
    player_email = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    def __str__(self):
        return self.player_name



class Game(models.Model):
    user = ForeignKey(Player,on_delete=models.CASCADE)
    game = models.CharField(max_length=50)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.game