from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import Modelo_1_Serializer
from .models import Modelo_1

# Create your views here.
class Modelo_1_ViewSet(viewsets.ModelViewSet):
    queryset = Modelo_1.objects.all()
    serializer_class = Modelo_1_Serializer