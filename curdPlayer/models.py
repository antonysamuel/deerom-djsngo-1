from django.db import models

# Create your models here.
class Player(models.Model):
    id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=150)
    player_email = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    game = models.CharField(max_length=150)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.player_name
