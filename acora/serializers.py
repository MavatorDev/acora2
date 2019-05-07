from rest_framework import serializers
from .models import Partida 

class sPartida(serializers.ModelSerializer):
     class Meta:
         model= Partida
         fields=('codigo','estado','temporizador')

