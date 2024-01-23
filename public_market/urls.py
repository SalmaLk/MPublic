from django.urls import path
from .views import AutoriteListCreate, AutoriteRetrieveUpdateDelete, ContratListCreate, ContratRetrieveUpdateDelete, FournisseurListCreate, FournisseurRetrieveUpdateDelete, MarcheListCreate, MarcheRetrieveUpdateDelete, PiecedetacheeListCreate, PiecedetacheeRetrieveUpdateDelete, PpmListCreate, PpmRetrieveUpdateDelete, SoumissionListCreate, SoumissionRetrieveUpdateDelete

urlpatterns = [
    path('autorite', AutoriteListCreate.as_view(), name='autorite-list'),
    path('autorite/<int:pk>/', AutoriteRetrieveUpdateDelete.as_view(), name='autorite-detail'),
    path('contrat', ContratListCreate.as_view(), name='contrat-list'),
    path('contrat/<int:pk>/', ContratRetrieveUpdateDelete.as_view(), name='contrat-detail'),
    path('fournisseur', FournisseurListCreate.as_view(), name='fournisseur-list'),
    path('fournisseur/<int:pk>/', FournisseurRetrieveUpdateDelete.as_view(), name='fournisseur-detail'),
    path('marche/', MarcheListCreate.as_view(), name='marche-list'),
    path('marche/<int:id>/', MarcheRetrieveUpdateDelete.as_view(), name='marche-detail'),
    path('piecedetachee', PiecedetacheeListCreate.as_view(), name='piecedetachee-list'),
    path('piecedetachee/<int:pk>/', PiecedetacheeRetrieveUpdateDelete.as_view(), name='piecedetachee-detail'),
    path('ppm', PpmListCreate.as_view(), name='ppm-list'),
    path('ppm/<int:pk>/', PpmRetrieveUpdateDelete.as_view(), name='ppm-detail'),
    path('soumission', SoumissionListCreate.as_view(), name='soumission-list'),
    path('soumission/<int:pk>/', SoumissionRetrieveUpdateDelete.as_view(), name='soumission-detail'),
]