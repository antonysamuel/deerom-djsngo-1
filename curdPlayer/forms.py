from django import forms
from django.forms import fields, models, widgets
from .models import Player

class AddPlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        exclude = ['id']
        widgets = {
            'player_name' : forms.TextInput(attrs={'class':'form-control'}),
            'player_email' : forms.TextInput(attrs={'class':'form-control','type' : 'email'}),
            'country' : forms.TextInput(attrs={'class':'form-control'}),
            # 'game' : forms.TextInput(attrs={'class':'form-control'}),
            # 'score' : forms.TextInput(attrs={'class':'form-control','type' : 'number'}),
        }