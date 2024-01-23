from django.shortcuts import render

from rest_framework import generics

from .models import Autorite, Contrat, Fournisseur, Marche, Piecedetachee, Ppm, Soumission

from .serializers import AutoriteSerializer, ContratSerializer, FournisseurSerializer, MarcheSerializer, PiecedetacheeSerializer, PpmSerializer, SoumissionSerializer

# Create your views here.

# Create an autorite and to display

class AutoriteListCreate(generics.ListCreateAPIView):

    queryset = Autorite.objects.all()
    serializer_class = AutoriteSerializer

# To retrieve, update or delete an autorite by ID
        
class AutoriteRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):

    queryset = Autorite.objects.all()
    serializer_class = AutoriteSerializer

class ContratListCreate(generics.ListCreateAPIView):
    
    queryset = Contrat.objects.all()
    serializer_class = ContratSerializer

class ContratRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):

    queryset = Contrat.objects.all()
    serializer_class = ContratSerializer

class FournisseurListCreate(generics.ListCreateAPIView):
    
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer

class FournisseurRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):

    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer

class MarcheListCreate(generics.ListCreateAPIView):
    
    queryset = Marche.objects.all()
    serializer_class = MarcheSerializer

class MarcheRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):

    queryset = Marche.objects.all()
    serializer_class = MarcheSerializer

class PiecedetacheeListCreate(generics.ListCreateAPIView):
    
    queryset = Piecedetachee.objects.all()
    serializer_class = PiecedetacheeSerializer

class PiecedetacheeRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):

    queryset = Piecedetachee.objects.all()
    serializer_class = PiecedetacheeSerializer

class PpmListCreate(generics.ListCreateAPIView):
    
    queryset = Ppm.objects.all()
    serializer_class = PpmSerializer

class PpmRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):

    queryset = Ppm.objects.all()
    serializer_class = PpmSerializer

class SoumissionListCreate(generics.ListCreateAPIView):
    
    queryset = Soumission.objects.all()
    serializer_class = SoumissionSerializer

class SoumissionRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):

    queryset = Soumission.objects.all()
    serializer_class = SoumissionSerializer