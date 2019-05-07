from django.http import JsonResponse
from rest_framework import generics
from .models import Equipo
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .serializers import sPartida

class equiposPartida(APIView):

    def get(self,request,pk):
        equipos = Equipo.objects.filter(codigo=pk).values_list('cod','nombre')
        equipos = list(equipos)
             
        return Response(equipos)

    def post(request):
        pass

class crearPartida(APIView):
 
     def post(self,request):
         serializer=sPartida(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
