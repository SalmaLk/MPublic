from rest_framework import serializers 


from .models import Autorite, Contrat, Fournisseur, Marche, Piecedetachee, Ppm, Soumission


class AutoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autorite
        fields = '__all__'

class ContratSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrat
        fields = '__all__'

class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fournisseur
        fields = '__all__'

class MarcheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marche
        fields = '__all__'

class PiecedetacheeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piecedetachee
        fields = '__all__'

class PpmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ppm
        fields = '__all__'

class SoumissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soumission
        fields = '__all__'