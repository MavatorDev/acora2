from django.urls import path
from . views import equiposPartida
from . views import crearPartida
from django.http import HttpResponse

urlpatterns = [ 
        path('equiposPartida/<int:pk>',equiposPartida.as_view(), name='equiposPartida'),
        path('crearPartida',crearPartida.as_view(), name='crearPartida'), 
       ]
	
